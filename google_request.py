import re

from decouple import config
import google.generativeai as genai


GOOGLE_API_KEY=config("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Настройки генерации
generation_config = genai.types.GenerationConfig(
    temperature=0.9,
    top_p=0.8,
    top_k=40,
    max_output_tokens=1024,
)

# Настройки безопасности
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH", 
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Используйте одну из доступных моделей:
model = genai.GenerativeModel(
    model_name='models/gemini-2.0-flash',
    generation_config=generation_config,
    safety_settings=safety_settings
)

convo = model.start_chat(history=[])


def format_response(text):
    clean_text = text

    # Убираем Markdown разметку
    clean_text = re.sub(r'\*\*(.*?)\*\*', r'\1', clean_text)
    clean_text = re.sub(r'\*(.*?)\*', r'\1', clean_text) 
    clean_text = re.sub(r'_(.*?)_', r'\1', clean_text)
    
    # Заменяем маркеры списков на переносы строк
    clean_text = clean_text.replace("* ", "\n• ")
    clean_text = clean_text.replace("• ", "\n• ")
    
    # Убираем все обратные слеши
    clean_text = clean_text.replace('\\"', '"')
    clean_text = clean_text.replace("\\'", "'")
    clean_text = clean_text.replace('\\\\"', '"')
    clean_text = clean_text.replace('\\\\', '\\')
    clean_text = clean_text.replace('\\', '')

    clean_text = re.sub(r'\n\s+', '\n', clean_text)
    clean_text = re.sub(r'[ \t]+', ' ', clean_text)
    clean_text = clean_text.replace('\n', '<br>')

    return clean_text

def get_quick_response(message):
    response = model.generate_content(message)
    return format_response(response.text)

def get_chat_response(message):
    convo.send_message(message)
    return format_response(convo.last.text)
