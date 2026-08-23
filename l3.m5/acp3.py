import requests
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO

model = "stabilityai/stable-diffusion-xl-base-1.0"

url = f"https://router.huggingface.co/hf-inference/models/{model}"

api = ""

prompt = input("Enter your image theme/prompt: ")

payload = {
    "inputs": prompt
}

headers = {
    "Authorization": f"Bearer {api}",
    "Content-Type": "application/json"
}

print("\nGenerating image...")

response = requests.post(
    url,
    headers=headers,
    json=payload
)


if response.status_code != 200:
    print("Error:", response.status_code)
    print(response.text)
    exit()

image = Image.open(BytesIO(response.content)).convert("RGB")

print("Image generated successfully!")

brightness = ImageEnhance.Brightness(image)
image = brightness.enhance(1.15)

contrast = ImageEnhance.Contrast(image)
image = contrast.enhance(1.20)

color = ImageEnhance.Color(image)
image = color.enhance(1.25)

sharpness = ImageEnhance.Sharpness(image)
image = sharpness.enhance(1.40)
image = image.filter(ImageFilter.SMOOTH)

image.show()


choice = input("\nDo you want to save the enhanced image? (y/n): ").strip().lower()

if choice == "y":
    output = "enhanced_ai_image.jpg"
    image.save(output, quality=95)
    print("Image saved as:", output)
else:
    print("Image was not saved.")

print("\nImage enhancement pipeline completed!")