import speech_recognition as sr
from googletrans import Translator
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""


def translate(text, language):
    translator = Translator()
    result = translator.translate(text, dest=language)
    return result.text


def main():
    print("Welcome to Voice Translation Assistant")

    language = input(
        "Enter language code (es=Spanish, fr=French, hi=Hindi, "
        "de=German, ja=Japanese): "
    )

    while True:
        choice = input("\nPress Enter to speak or type exit: ")

        if choice.lower() == "exit":
            print("Assistant stopped")
            break

        text = listen()

        if text == "":
            continue

        translated_text = translate(text, language)

        print("Translated text:", translated_text)

        speak(translated_text)


main()