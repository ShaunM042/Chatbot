# modules/session_manager.py
import json
from datetime import datetime

HISTORY_FILE = 'session_history.json'

def load_history_from_file():
    try:
        with open(HISTORY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []

def save_history_to_file(session_history):
    with open(HISTORY_FILE, 'w') as file:
        json.dump(session_history, file, indent=4)

def save_message_to_session(session_id, message, response):
    session_history = load_history_from_file()
    # Find the session or create a new one if it does not exist
    session = next((s for s in session_history if s['sessionId'] == session_id), None)
    if not session:
        session = {'sessionId': session_id, 'messages': []}
        session_history.append(session)

    # Append the new message and response to the session
    session['messages'].append({
        'message': message,
        'response': response,
        'timestamp': datetime.now().isoformat()
    })
    
    # Save the updated history back to the file
    save_history_to_file(session_history)