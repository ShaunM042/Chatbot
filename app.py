from datetime import datetime
from flask import Flask, request, jsonify, render_template
from chatbot import get_intent, generate_response, tokenize_input, save_message_to_session, load_history_from_file

app = Flask(__name__)

# Initialize a session ID for each session
currentSessionId = datetime.now().isoformat()

# Load the history when the app starts
session_history = load_history_from_file()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    tokens = tokenize_input(user_input)
    intent = get_intent(tokens)
    response = generate_response(intent, tokens)

    # Save the message to the session
    save_message_to_session(currentSessionId, user_input, response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5030)