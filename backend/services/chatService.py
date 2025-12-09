from openai import OpenAI
import os

class ChatService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.conversations = {}
    
    def process_message(self, message, conversation_id, user_id):
        """Process user message and generate AI response"""
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        
        # Add user message to conversation history
        self.conversations[conversation_id].append({
            'role': 'user',
            'content': message
        })
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model='gpt-4',
                messages=self.conversations[conversation_id],
                temperature=0.7,
                max_tokens=500
            )
            
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversations[conversation_id].append({
                'role': 'assistant',
                'content': assistant_message
            })
            
            return {
                'response': assistant_message,
                'conversation_id': conversation_id
            }
        except Exception as e:
            return {
                'error': str(e),
                'response': 'Sorry, I encountered an error. Please try again.'
            }
    
    def get_conversation_history(self, conversation_id):
        """Get conversation history"""
        return self.conversations.get(conversation_id, [])
    
    def clear_conversation(self, conversation_id):
        """Clear conversation history"""
        if conversation_id in self.conversations:
            del self.conversations[conversation_id]
            return True
        return False
