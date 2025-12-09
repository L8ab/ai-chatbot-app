import unittest
from services.chatService import ChatService

class TestChatService(unittest.TestCase):
    def setUp(self):
        self.chat_service = ChatService()
    
    def test_process_message(self):
        result = self.chat_service.process_message(
            "Hello",
            "test_conv_1",
            "user_1"
        )
        self.assertIn('response', result)
    
    def test_get_conversation_history(self):
        self.chat_service.process_message("Test", "conv_1", "user_1")
        history = self.chat_service.get_conversation_history("conv_1")
        self.assertGreater(len(history), 0)
