import base64
import requests
from datetime import datetime

api = ""

url = "https://router.huggingface.co/v1/chat/completions"

models = [
    "zai-org/GLM-4.5V",
    "Qwen/Qwen2.5-VL-72B-Instruct",
    "Qwen/Qwen2.5-VL-32B-Instruct"
]

headers = {
    "Authorization": f"Bearer {api}",
    "Content-Type": "application/json"
}

report = []

while True:
    img = input("\nEnter image path (or type 'exit' to finish): ")

    if img.lower() == "exit":
        break

    try:
        with open(img, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()

        caption = None

        for model in models:
            print("\nTrying:", model)

            payload = {
                "model": model,
                "messages": [{
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Give a short and clear caption for this image."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{b64}"
                            }
                        }
                    ]
                }]
            }

            r = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=120
            )

            if r.status_code == 200:
                caption = r.json()["choices"][0]["message"]["content"]
                print("Caption:", caption)

                report.append({
                    "image": img,
                    "caption": caption,
                    "model": model,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

                break
            else:
                print("It failed:", r.status_code)

        if caption is None:
            print("Could not generate a caption.")

    except FileNotFoundError:
        print("Image not found. Please enter a valid path.")

with open("caption_report.txt", "w", encoding="utf-8") as f:
    f.write("IMAGE CAPTIONING REPORT\n")
    f.write("=" * 60 + "\n\n")

    for item in report:
        f.write("Image: " + item["image"] + "\n")
        f.write("Caption: " + item["caption"] + "\n")
        f.write("Model: " + item["model"] + "\n")
        f.write("Time: " + item["time"] + "\n")
        f.write("-" * 60 + "\n")

print("\nCaptioning completed.")
print("Report saved as caption_report.txt")