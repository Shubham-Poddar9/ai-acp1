import random

destination = {
    "beaches": ["Bali", "Phuket", "Maldives", "Goa"],
    "mountains": ["Everest", "K2", "Annapurna", "Himalayas"],
    "cities": ["Kathmandu", "Pokhara", "Paris", "Dubai"],
    "adventure": ["Bungee Jumping in Nepal", "Skydiving in Dubai"]
}

jokes = [
    "Why don’t mountains get tired? Because they peak.",
    "I tried to catch fog. Mist.",
    "Why did the beach blush? Because of the sea weed."
]

def recommend():
    print("I can suggest: beaches, mountains, cities, adventure")
    choice = input("where do yo what to go? ").lower()

    if choice in destination:
        print("You could try", random.choice(destination[choice]))
    else:
        print("I did not understand that")

def packing():
    days = input("How many days? ")
    place = input("Where are you going? ")
    print(f"{place} for {days} days sounds like a good plan")

def chat():
    print("Hello, I am your chatbot")

    while True:
        msg = input("What do you need? ").lower()

        if "recommend" in msg:
            recommend()

        elif "joke" in msg:
            print(random.choice(jokes))

        elif "packing" in msg:
            packing()

        elif msg in ["exit", "bye"]:
            print("Goodbye")
            break

        else:
            print("You can say recommend, joke, packing or exit")

chat()