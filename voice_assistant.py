import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please try again.")
        return ""
    except sr.RequestError:
        speak("Sorry, there's an issue with the speech service.")
        return ""

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you?")

def process_command(command):
    if 'hello' in command:
        speak("Hello! How can I help you?")

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif 'date' in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {date}")

    elif 'search' in command:
        speak("What would you like to search for?")
        query = listen()
        if query:
            speak(f"Searching for {query} on the web.")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    elif 'wikipedia' in command:
        speak("What should I search on Wikipedia?")
        topic = listen()
        if topic:
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak("According to Wikipedia:")
                speak(summary)
            except:
                speak("Sorry, I couldn't find that on Wikipedia.")

    elif 'exit' in command or 'stop' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I don't understand that yet.")

def main():
    greet()
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
