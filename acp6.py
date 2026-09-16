import pyttsx3
import speech_recognition as sr
from googletrans import Translator

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    engine.runAndWait()

def translate_text(text, source_language, target_language):
    translator = Translator()
    translated = translator.translate(
        text,
        src=source_language,
        dest=target_language
    )
    return translated.text

def select_language(message):
    print("\nAvailable Languages:")
    print("1. English (en)")
    print("2. French (fr)")
    print("3. German (de)")
    print("4. Spanish (es)")
    print("5. Italian (it)")
    print("6. Portuguese (pt)")
    print("7. Hindi (hi)")
    print("8. Nepali (ne)")

    choice = input(message)

    language_dict = {
        "1": "en",
        "2": "fr",
        "3": "de",
        "4": "es",
        "5": "it",
        "6": "pt",
        "7": "hi",
        "8": "ne"
    }

    return language_dict.get(choice, "en")

def recognize_speech(source_language):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(
            audio,
            language=source_language
        )
        print("You:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return None

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return None

    except Exception as e:
        print("Error:", e)
        return None

def main():
    print("===== Speech Translation Application =====")

    source_language = select_language(
        "Select source language (1-8): "
    )

    target_language = select_language(
        "Select target language (1-8): "
    )

    print("\nStart speaking...")
    original_text = recognize_speech(source_language)

    if original_text:
        try:
            translated_text = translate_text(
                original_text,
                source_language,
                target_language
            )

            print("Translation:", translated_text)
            speak(translated_text)

        except Exception as e:
            print("Translation error:", e)

if __name__ == "__main__":
    main()