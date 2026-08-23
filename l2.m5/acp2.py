from huggingface_hub import InferenceClient
from datetime import datetime
from PIL import ImageEnhance, ImageFilter

models = [
    "black-forest-labs/FLUX.1-schnell",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    "CompVis/stable-diffusion-v1-4"
]

api = ""

client = InferenceClient(api_key=api)

print("Primary model:", models[0])
print("Type 'q' to exit")

def enhance_image(image):
    print("\nChoose enhancement settings:")

    brightness = float(input("Brightness (1.0 = normal): ") or 1.5)
    contrast = float(input("Contrast (1.0 = normal): ") or 1.3)
    sharpness = float(input("Sharpness (1.0 = normal): ") or 1.5)
    blur = float(input("Blur radius (0 = none): ") or 0)

    image = ImageEnhance.Brightness(image).enhance(brightness)

    image = ImageEnhance.Contrast(image).enhance(contrast)

    image = ImageEnhance.Sharpness(image).enhance(sharpness)

    if blur > 0:
        image = image.filter(
            ImageFilter.GaussianBlur(radius=blur)
        )

    return image


while True:

    prompt = input("\nEnter your image prompt: ").strip()

    if prompt.lower() == "q":
        print("Program exited.")
        break

    if not prompt:
        print("Please enter a prompt.")
        continue

    print("\nGenerating image...")
    image = None

    for model in models:
        try:
            print("Trying model:", model)

            image = client.text_to_image(
                prompt=prompt,
                model=model
            )

            print("Image generated successfully!")
            break

        except Exception as e:
            print("Error with", model)
            print(e)

    if image is not None:

        try:
            print("\nApplying image enhancements...")

            image = enhance_image(image)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = f"enhanced_image_{timestamp}.jpg"

            image.save(filename, "JPEG")

            print("\nImage enhancement completed!")
            print("Saved as:", filename)

            image.show()

        except Exception as e:
            print("Error while processing image:", e)

    else:
        print("\nAll models failed.")
        print("Please check your API key, internet connection, or model availability.")