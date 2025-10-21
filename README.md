# Telegram Music Bot

Telegram-бот для разделения музыкальных треков на стемы (вокал, барабаны, бас, остальные инструменты) с использованием нейросети Demucs.

## 🎯 Описание проекта

Бот позволяет пользователям загружать аудиофайлы и получать обратно разделенные стемы для дальнейшего использования в музыкальном производстве, ремиксинге или караоке.

## 🛠 Технический стек

- **Python 3.11+**
- **aiogram 3.x** - асинхронная библиотека для Telegram Bot API
- **Demucs 4.0** - нейросеть для разделения аудио на стемы
- **PyTorch** - фреймворк машинного обучения
- **Poetry** - управление зависимостями
- **Docker** - контейнеризация
- **pytest** - тестирование
- **flake8** - проверка стиля кода

## 📁 Структура проекта

```
telegram-music-bot/
├── src/
│   ├── __init__.py
│   ├── bot.py              # Основная логика бота
│   ├── audio_processor.py  # Обработка аудио через Demucs
│   └── utils.py           # Вспомогательные функции
├── tests/
│   ├── __init__.py
│   ├── test_bot.py
│   └── test_audio_processor.py
├── docker/
│   └── Dockerfile
├── .github/
│   └── workflows/
│       └── ci.yml         # CI/CD pipeline
├── pyproject.toml         # Конфигурация Poetry
├── docker-compose.yml
├── .env.example
└── README.md
```

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.11+
- Poetry
- Docker (опционально)
- Telegram Bot Token (получить у [@BotFather](https://t.me/botfather))

### Локальная разработка

1. **Клонирование репозитория:**
```bash
git clone https://github.com/nike4192/telegram-music-bot.git
cd telegram-music-bot
```

2. **Установка зависимостей:**
```bash
poetry install
```

3. **Настройка окружения:**
```bash
cp .env.example .env
# Отредактируйте .env файл, добавив ваш TELEGRAM_BOT_TOKEN
```

4. **Запуск бота:**
```bash
poetry run python -m src.main
```

### Запуск через Docker

1. **Настройка окружения:**
```bash
cp .env.example .env
# Добавьте ваш TELEGRAM_BOT_TOKEN в .env файл
```

2. **Запуск контейнера:**
```bash
docker-compose up --build
```

## 🧪 Тестирование

### Запуск тестов
```bash
poetry run pytest tests/
```

### Проверка стиля кода
```bash
poetry run flake8 src/ --max-line-length=88
```

### Запуск всех проверок
```bash
poetry run pytest tests/ && poetry run flake8 src/ --max-line-length=88
```

## 🔄 Процесс разработки

### Работа с ветками
1. Создайте новую ветку для фичи:
```bash
git checkout -b feature/your-feature-name
```

2. Внесите изменения и зафиксируйте:
```bash
git add .
git commit -m "feat: add your feature description"
```

3. Отправьте ветку в репозиторий:
```bash
git push origin feature/your-feature-name
```

4. Создайте Pull Request для Code Review

### Code Review
- Все изменения должны проходить через Pull Request
- Требуется одобрение минимум одного разработчика
- CI проверки должны пройти успешно

## 📊 CI/CD

Настроен автоматический pipeline в GitHub Actions, который выполняет:
- Установку зависимостей
- Запуск unit тестов
- Проверку соответствия PEP8
- Проверку при каждом push и Pull Request

## 🚀 Деплой

Приложение готово к развертыванию на облачных платформах:
- Яндекс.Облако
- AWS
- Google Cloud Platform

Конфигурация Docker позволяет легко развернуть бота в любой облачной среде.

## 📝 Использование

1. Найдите бота в Telegram по имени или ссылке
2. Отправьте команду `/start`
3. Загрузите аудиофайл (поддерживаемые форматы: MP3, WAV, FLAC)
4. Дождитесь обработки (обычно 2-5 минут)
5. Получите разделенные стемы:
   - `vocals.wav` - вокальная партия
   - `drums.wav` - барабаны
   - `bass.wav` - бас-линия
   - `other.wav` - остальные инструменты

## 📄 Лицензия

Этот проект создан в учебных целях.

## 🐛 Известные ограничения

- Максимальный размер файла: 50MB (ограничение Telegram)
- Время обработки зависит от длительности трека
- Качество разделения зависит от исходного материала
