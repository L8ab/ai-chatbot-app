from flask import Flask, request, jsonify
from flask_cors import CORS
from services.chatService import ChatService
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

chat_service = ChatService()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    result = chat_service.process_message(
        data.get('message'),
        data.get('conversation_id'),
        data.get('user_id')
    )
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
