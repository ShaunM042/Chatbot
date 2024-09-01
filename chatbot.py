import logging
from datetime import datetime
from modules.interaction_manager import InteractionManager
from modules.session_manager import load_history_from_file, save_history_to_file, save_message_to_session
from modules.utilities import setup_logging

# Set up logging
setup_logging()

# Load session history when the app starts
session_history = load_history_from_file()

def main():
    interaction_manager = InteractionManager()

    while True:
        user_input = input("You: ")
        response, session_update = interaction_manager.handle_input(user_input)
        
        print("Chatbot:", response)
        
        # If there is any session data to update
        if session_update:
            save_message_to_session(session_update['session_id'], user_input, response)
            save_history_to_file(session_history)

if __name__ == "__main__":
    main()