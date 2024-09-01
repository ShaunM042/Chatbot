# modules/nlp.py
import spacy
from transformers import pipeline

# Load the SpaCy language model
nlp = spacy.load('en_core_web_sm')

# Initialize a text-generation pipeline with DialoGPT
nlp_model = pipeline("text-generation", model="microsoft/DialoGPT-medium", framework="pt")
transformer = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def process_input(user_input, context):
    """Process the user input to determine the intent and extract tokens."""
    doc = nlp(user_input.lower())
    tokens = [token.text for token in doc]
    intent = determine_intent(tokens, context)
    update_context(intent, context)
    return intent, tokens

def determine_intent(tokens, context):
    """Determine the user's intent based on tokens."""
    intent_keywords = {
        'greeting': ['hello', 'hi', 'hey', 'greetings'],
        'time': ['time', 'clock', 'hour'],
        'help': ['help', 'assist', 'support'],
        'small_talk': ['how', 'feel', 'joke', 'name'],
        'fact': ['fact', 'information', 'tell', 'something'],
        'weather': ['weather', 'forecast', 'temperature', 'in'],
        'compliment': ['smart', 'amazing', 'awesome'],
        'insult': ['dumb', 'stupid', 'idiot'],
        'math': ['calculate', 'plus', 'minus', 'add', 'subtract', 'multiply', 'divide', 'times', 'by'],
        'news': ['news', 'headlines', 'latest'],
        'translation': ['translate', 'translation', 'to']
    }
    for intent, keywords in intent_keywords.items():
        if any(word in tokens for word in keywords):
            return intent
    return 'unknown'

def update_context(intent, context):
    """Update the context based on the determined intent."""
    if intent == 'greeting':
        context['was_greeted'] = True
    elif intent == 'goodbye':
        context['end_conversation'] = True
    # Add other context updates as necessary

def generate_nlp_response(tokens):
    """Generate a response using NLP model based on the processed tokens."""
    prompt = " ".join(tokens)
    response = nlp_model(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']