import speech_recognition as sr
from googletrans import Translator

def stt():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("speak in hindi language ")
        audio=r.listen(source)


    try:
        text=r.recognize_google(audio,language="hi")
        print("you said: ",text)
        return text

    except:
        print("could not understand ")
        return""


def tt(text):
    translator = Translator()
    result=translator.translate(text,src="hi",dest="en")
    print("this is traslated text in english language:- ",result.text)

text=stt()

if text:
    tt(text)