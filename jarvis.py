import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        question = input("You: ")
        if question.lower() == 'q':
            break
        response = get_response(question)

        print("Bot:", response)
        speak(response)


def get_response(question):
    if question.lower() == 'how are you?':
        return "I'm good, thank you!"
    elif question.lower() == 'what is your name?':
        return "I am Jarvis, a language model developed by Sathwik."
    else:
        return "I'm sorry, I don't have an answer for that."


if __name__ == '__main__':
    speak("Hello! How can I assist you today?")
    main()
