AUTHOR = "Arian Nunez"
APP_NAME = "Uppercase-Lowercase Converter"

def run():
    message = "Hello from Students Arcade"

    original = message
    upper = message.upper()
    lower = message.lower()

    result = "Original: " + original
    result = result + " | Uppercase: " + upper
    result = result + " | Lowercase: " + lower

    return result