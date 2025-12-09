# AI Chatbot Application

An intelligent chatbot application powered by OpenAI GPT models with conversation history management.

## Features

- Natural language conversations
- Conversation history tracking
- OpenAI GPT-4 integration
- RESTful API
- React frontend ready

## Tech Stack

- **Backend**: Python, Flask
- **AI**: OpenAI API (GPT-4)
- **Frontend**: React with TypeScript
- **Database**: In-memory conversation storage

## Project Structure

\`\`\`
ai-chatbot-app/
├── backend/
│   ├── services/        # Chat service
│   ├── utils/           # Helper functions
│   └── app.py           # Flask application
├── frontend/
│   └── src/
│       └── hooks/       # React hooks
├── tests/               # Test files
└── requirements.txt
\`\`\`

## Installation

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Configuration

Set your OpenAI API key:

\`\`\`
OPENAI_API_KEY=your-api-key
\`\`\`

## Running

\`\`\`bash
python backend/app.py
\`\`\`

## API Endpoints

- \`POST /api/chat\` - Send message to chatbot
- \`GET /health\` - Health check

---

**POWERED BY L8AB SYSTEMS**
