# VK Image Echo Bot

Этот бот для ВКонтакте отправляет приветственное сообщение пользователю при первом взаимодействии и возвращает отправленные изображения обратно. Бот игнорирует любые другие сообщения.

## Установка

### 1. Клонируйте репозиторий

Сначала клонируйте репозиторий на ваш компьютер:

```bash
git clone https://github.com/Temmmmmo/vk-bot.git
cd vk_bot
```

### 2. Установите зависимости

Убедитесь, что у вас установлен Python 3.6 или выше. Установите необходимые библиотеки с помощью `pip`:

```bash
pip install -r requirements.txt
text
```

### 3. Получение токена и ID группы

Для работы бота вам понадобятся следующие переменные окружения:

- **VK_API_TOKEN**: Токен доступа вашего сообщества ВКонтакте.
- **VK_GROUP_ID**: ID вашего сообщества (число, без минуса).

#### Как получить токен и ID группы:

1. **Создайте сообщество**:
   - Перейдите на [страницу создания сообщества](https://vk.com/groups?act=create).
   - Заполните необходимые поля и создайте сообщество.

2. **Получите токен доступа**:
   - Перейдите в настройки вашего сообщества.
   - Найдите раздел "Работа с API" и выберите "Ключи доступа".
   - Нажмите "Добавить ключ" и выберите необходимые права (например, "Отправка сообщений").
   - Сохраните сгенерированный токен.

3. **Получите ID группы**:
   - ID группы можно найти в адресной строке браузера, когда вы находитесь на странице вашего сообщества. Например, если URL выглядит как `https://vk.com/club123456`, то ваш ID — `123456`.

### 4. Настройка переменных окружения

Создайте файл `.env` в корневом каталоге проекта и добавьте следующие строки:
```dotenv
VK_API_TOKEN=ваш_токен_доступа
VK_GROUP_ID=ваш_id_группы
```

### 5. Запуск бота

Теперь вы готовы запустить бота! Используйте следующую команду:
```bash
python vk_bot.py
```

## Структура проекта

- `vk_bot.py`: Основной файл бота.
- `settings.py`: Файл, содержащий конфигурационную модель
- `requirements.txt`: Список зависимостей проекта.
- `.env`: Файл с переменными окружения (не забудьте добавить его в `.gitignore`, чтобы не публиковать свои токены).

---

Если у вас есть вопросы или проблемы, не стесняйтесь обращаться!
