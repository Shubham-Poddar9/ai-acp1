import requests

HF_API_KEY = ""

MODEL_ID = "facebook/bart-large-mnli"

API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}
LABELS = ["Spam", "Safe"]


def check_message(message):
    payload = {
        "inputs": message,
        "parameters": {
            "candidate_labels": LABELS
        }
    }

    response = requests.post(
        API_URL,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    if not response.ok:
        raise RuntimeError(
            f"HF Error {response.status_code}: {response.text}"
        )

    return response.json()


def show_result(message, predictions):
    best = max(predictions, key=lambda x: x["score"])

    label = best["label"]
    confidence = best["score"] * 100

    print("\n" + "=" * 55)
    print("           AI SPAM MESSAGE CLASSIFIER")
    print("=" * 55)

    print("Message:", message)
    print(f"Result: {label}")
    print(f"Confidence: {confidence:.1f}%")

    print("\nPredictions:")

    for prediction in predictions:
        score = prediction["score"] * 100
        print(f"{prediction['label']}: {score:.1f}%")

    print("=" * 55)


def main():
    print("=" * 55)
    print("        WELCOME TO AI SPAM CLASSIFIER")
    print("=" * 55)
    print("Enter a message and AI will classify it.")
    print("Type 'exit' to stop.\n")

    while True:
        message = input("Message: ").strip()

        if message.lower() == "exit":
            print("\nGoodbye! Keep coding!")
            break

        if not message:
            print("Please enter a message.\n")
            continue

        try:
            predictions = check_message(message)

            if isinstance(predictions, list):
                show_result(message, predictions)
            else:
                print("Unexpected response:", predictions)

        except Exception as error:
            print("\nSomething went wrong.")
            print("Reason:", error)
            print("Check your API key and internet connection.\n")


if __name__ == "__main__":
    main()