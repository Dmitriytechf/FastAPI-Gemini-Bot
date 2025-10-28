# Fast API Gemini Bot

Проект на FastAPI: реализация *двух AI-ботов*. Первый бот обрабатывает универсальные запросы без сохранения контекста, второй поддерживает диалог, запоминая историю общения.

## 🚀 Стек технологий

### Backend
- **FastAPI** (0.120.1) - современный веб-фреймворк для Python
- **Uvicorn** (0.38.0) - ASGI сервер для запуска приложения
- **Python-decouple** (3.8) - управление конфигурацией через .env файлы

### AI & Machine Learning
- **Google Generative AI** (0.8.5) - интеграция с Gemini API
- **Google AI Generativelanguage** (0.6.15) - клиент для работы с Gemini моделями
- **Protobuf** (5.29.5) - сериализация данных для Google API

### Frontend & UI
- **Tailwind CSS** (через CDN) - утилитарный CSS фреймворк
- **HTMX** (1.9.10) - библиотека для динамического обновления контента
- **Jinja2** (3.1.6) - шаблонизатор для HTML

## Внешний вид
<img width="1513" height="899" alt="image" src="https://github.com/user-attachments/assets/aa7cd33c-1045-4d97-ae50-1f83e5ab6f5b" />
<img width="1444" height="883" alt="image" src="https://github.com/user-attachments/assets/8336fc84-a342-4447-8e6c-4d5cddbe94de" />

## 🛠 Установка и запуск
1. **Клонирование и настройка окружения:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
2. Настройка переменных окружения
# .env файл
GOOGLE_API_KEY=your_gemini_api_key_here
3. Запуск приложения командой:
```bash
uvicorn main:app --reload
```
