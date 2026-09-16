import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.setProperty("volume", 1.0)

    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def reco():
    r = sr.Recognizer()

    with sr.Microphone() as src:
        print("Listening...")
        r.adjust_for_ambient_noise(src, duration=0.5)

        try:
            audio = r.listen(src, timeout=8)

        except sr.WaitTimeoutError:
            print("Time out, try again")
            return ""

    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Sorry, I could not understand you")
        speak("Sorry, I could not understand you")
        return ""

    except sr.RequestError:
        print("Speech recognition service is not available")
        speak("Speech recognition service is not available")
        return ""


def respond(command):

    if "name" in command:
        speak("My name is Jarvis.")

    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "how are you" in command:
        speak("I am doing great. Thank you for asking!")

    elif "exit" in command or "stop" in command or "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, I don't know that command.")

    return True


def main():
    print("Welcome to Jarvis Voice Assistant!")
    speak("Hello! I am Jarvis. How can I help you?")

    while True:
        command = reco()

        if command:
            if not respond(command):
                break


main()