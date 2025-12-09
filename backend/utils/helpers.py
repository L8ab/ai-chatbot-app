import re
from datetime import datetime

def sanitize_input(text):
    """Sanitize user input"""
    if not text:
        return ""
    # Remove potentially harmful characters
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def format_timestamp(timestamp):
    """Format timestamp to readable string"""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def validate_message(message):
    """Validate chat message"""
    if not message or len(message.strip()) == 0:
        return False, "Message cannot be empty"
    if len(message) > 1000:
        return False, "Message too long (max 1000 characters)"
    return True, None
