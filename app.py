from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'secret-key')
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Store conversation history
conversations = {}


@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK', 'message': 'AI Chatbot API is running'})


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.json
        user_id = data.get('user_id', 'default')
        message = data.get('message', '')
        conversation_id = data.get('conversation_id', None)

        # Get or create conversation history
        if conversation_id not in conversations:
            conversations[conversation_id] = []

        # Add user message to history
        conversations[conversation_id].append({
            'role': 'user',
            'content': message
        })

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=conversations[conversation_id],
            temperature=0.7,
            max_tokens=500
        )

        assistant_message = response.choices[0].message.content

        # Add assistant response to history
        conversations[conversation_id].append({
            'role': 'assistant',
            'content': assistant_message
        })

        return jsonify({
            'response': assistant_message,
            'conversation_id': conversation_id
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@socketio.on('message')
def handle_message(data):
    """Handle WebSocket messages"""
    user_id = data.get('user_id')
    message = data.get('message')
    conversation_id = data.get('conversation_id')

    # Process message and get response
    # Similar logic to /api/chat endpoint

    emit('response', {
        'message': 'Response from chatbot',
        'conversation_id': conversation_id
    })


@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    """Get all conversations for a user"""
    user_id = request.args.get('user_id')
    # Return user's conversations
    return jsonify({'conversations': []})


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)

