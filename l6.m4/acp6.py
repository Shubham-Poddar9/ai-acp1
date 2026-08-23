import requests
from colorama import Fore, init

init(autoreset=True)

API_KEY = ""
URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

def summarize(text, min_length=30, max_length=100):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length
        }
    }

    try:
        response = requests.post(URL, headers=headers, json=data)
        result = response.json()

        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]["summary_text"]

        return "Could not generate summary."

    except Exception as e:
        return f"Error: {e}"


print(Fore.MAGENTA + "=" * 50)
print(Fore.MAGENTA + "       TEXT SUMMARIZER")
print(Fore.MAGENTA + "=" * 50)

name = input(Fore.GREEN + "Enter your name: ").strip().title()

print(Fore.CYAN + "\nEnter the text you want to summarize:")
text = input().strip()

if not text:
    print(Fore.RED + "No text entered!")
else:
    print(Fore.YELLOW + "\nChoose summary length:")
    print("1. Short")
    print("2. Medium")
    print("3. Long")

    choice = input(Fore.GREEN + "Enter choice (1/2/3): ").strip()

    if choice == "1":
        minimum = 15
        maximum = 50
    elif choice == "2":
        minimum = 30
        maximum = 100
    elif choice == "3":
        minimum = 50
        maximum = 150
    else:
        print(Fore.RED + "Invalid choice. Using medium length.")
        minimum = 30
        maximum = 100

    print(Fore.YELLOW + "\nGenerating summary...")

    summary = summarize(text, minimum, maximum)

    print(Fore.MAGENTA + "\n" + "=" * 50)
    print(Fore.LIGHTGREEN_EX + f"Summary for {name}:")
    print(Fore.WHITE + summary)
    print(Fore.MAGENTA + "=" * 50)