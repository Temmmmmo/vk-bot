import os

import requests
import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

from settings import Settings, get_settings

settings: Settings = get_settings()


def download_image(url: str) -> str | None:
    """Скачивает изображение по URL и возвращает путь к сохраненному файлу."""
    response = requests.get(url)
    if response.status_code == 200:
        file_path = "temp_image.jpg"
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path


def main():
    vk_session = vk_api.VkApi(token=settings.VK_API_TOKEN)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, settings.VK_GROUP_ID)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.message.from_id
            if event.message.attachments:
                for attachment in event.message.attachments:
                    if attachment["type"] == "photo":
                        photo_sizes = attachment["photo"]["sizes"]
                        largest_photo = max(photo_sizes, key=lambda x: x["width"])
                        photo_url = largest_photo["url"]
                        temp_path = download_image(photo_url)

                        if temp_path:
                            upload = vk_api.VkUpload(vk_session)
                            photo = upload.photo_messages(photos=temp_path)[0]
                            vk.messages.send(
                                user_id=user_id,
                                attachment=f'photo{photo["owner_id"]}_{photo["id"]}',
                                random_id=0,
                                reply_to=event.message.id,
                            )
                            os.remove(temp_path)


if __name__ == "__main__":
    main()
