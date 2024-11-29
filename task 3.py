import nltk
from nltk.chat.util import Chat, reflections

# Ensure the NLTK data is downloaded
nltk.download('punkt')

# Define the chatbot pairs: patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hi there! How can I help you?']),
    (r'how are you?', ['I am just a bot, but I am doing well! How about you?']),
    (r'what is your name?', ['I am a chatbot. You can call me ChatBot.']),
    (r'bye|goodbye', ['Goodbye! Have a great day!', 'Bye! Talk to you soon.']),
    (r'(.*) your name?', ['I am a chatbot, and I don’t have a personal name.']),
    (r'what can you do?', ['I can chat with you, answer questions, and have simple conversations.']),
    (r'(.*) help (.*)', ['I am here to help you! What do you need assistance with?']),
    (r'(.*)', ['I am not sure how to respond to that, but I am here to chat!'])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to start the chatbot conversation
def start_chat():
    print("ChatBot: Hi! I'm here to chat with you. Type 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye! Take care!")
            break
        
        # Generate a response
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
