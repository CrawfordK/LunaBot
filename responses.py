def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Yo!'
    
    return "What are you trying to do bro? I can\'t understand what you said."