from decouple import config
import google.generativeai as genai


GOOGLE_API_KEY=config("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Проверка доступных моделей
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)
