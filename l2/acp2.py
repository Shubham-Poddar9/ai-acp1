from textblob import TextBlob
from colorama import Fore, init
init()

pos = neg = neu = 0
history = []

while True:
    text = input("You: ")

    if text == "exit":
        print("Final:", pos, neg, neu)
        break
    elif text == "stats":
        print("Positive:", pos, "Negative:", neg, "Neutral:", neu)
    elif text == "history":
        print(history)
    elif text == "reset":
        pos = neg = neu = 0
        history.clear()
    else:
        p = TextBlob(text).sentiment.polarity

        if p > 0:
            print(Fore.GREEN + "Positive")
            pos += 1
            s = "Positive"
        elif p < 0:
            print(Fore.RED + "Negative")
            neg += 1
            s = "Negative"
        else:
            print("Neutral")
            neu += 1
            s = "Neutral"

        history.append((text, s))