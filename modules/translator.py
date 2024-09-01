# modules/translator.py
from googletrans import Translator

translator = Translator()

def translate_text(text, dest_language):
    try:
        result = translator.translate(text, dest=dest_language)
        return f"The translation is: {result.text}"
    except Exception as e:
        return f"Sorry, I couldn't translate that text. Error: {e}"