import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'What is your name?',
     ['My name is Clink AI Chat Bot.']),
    (r'What can you do?',
     ['I can answer your questions. Ask me something.']),
    (r'What is IT Project Management?',
     ['It refers to the practice of planning, organizing, and overseeing IT projects within an organization.']),
    (r'What should i learn to become a PM?',
     ['To become a PM, you should start learning Product Lifecycle Management, Agile and Scrum Methodologies.']),
    (r'Can you advise me some courses for PM?',
     ['Sure. QALight is having a cool PM course for beginners. ']),
    (r'Thank you for your answers!',
     ['Good luck on your journey!']),
]

chatbot = Chat(patterns, reflections)


def main():
    print('Welcome to the chat bot! How can we help you?')
    while True:
        user_input = input("You:")
        response = chatbot.respond(user_input)
        print("Chatbot: " + response)


if __name__ == "__main__":
    main()
