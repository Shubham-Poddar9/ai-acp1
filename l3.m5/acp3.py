import requests
from PIL import Image
from io import BytesIO

model = "stabilityai/stable-diffusion-2-inpainting"

url = f"https://router.huggingface.co/hf-inference/models/{model}"

api = ""

image_path = input("Enter the path of the vintage image: ")
mask_path = input("Enter the path of the mask image: ")

prompt = input("Enter a description for the damaged area: ")

with open(image_path, "rb") as image_file:
    image_data = image_file.read()

with open(mask_path, "rb") as mask_file:
    mask_data = mask_file.read()

headers = {
    "Authorization": f"Bearer {api}"
}

files = {
    "image": ("image.png", image_data, "image/png"),
    "mask_image": ("mask.png", mask_data, "image/png")
}

data = {
    "prompt": prompt
}

response = requests.post(
    url,
    headers=headers,
    files=files,
    data=data
)

if response.status_code != 200:
    print("Error:", response.text)
    exit()

result = Image.open(BytesIO(response.content))

result.show()

print("Do you want to save the restored image?")
choice = input("y or n: ").strip().lower()

if choice == "y":
    output = "restored_vintage_photo.png"
    result.save(output)
    print("Image is saved as", output)