import requests

api = ""

url = "https://router.huggingface.co/hf-inference/models/cardiffnlp/twitter-roberta-base-sentiment-latest"

headers = {
    "Authorization": f"Bearer {api}"
}

while True:
    sentence = input("Enter your sentence: ")

    if sentence.lower() == "exit":
        break

    payload = {
        "inputs": sentence
    }

    r = requests.post(
        url,
        headers=headers,
        json=payload
    )

    if r.ok:
        result = r.json()

        # Get the prediction with the highest score
        prediction = max(result[0], key=lambda x: x["score"])

        label = prediction["label"]
        score = prediction["score"]

        print("\nSentiment:", label)
        print("Confidence:", round(score * 100, 2), "%")

        if label == "positive":
            print(" This is a positive sentence.")

        elif label == "negative":
            print("This is a negative sentence.")

        else:
            print(" This is a neutral sentence.")

    else:
        print("Error:", r.status_code)
        print(r.text)