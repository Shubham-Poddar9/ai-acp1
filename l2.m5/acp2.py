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

print("AI Image Generation & Enhancement Pipeline")
print("Primary model:", models[0])
print("Enter 'q' to exit.\n")

def enhance_image(image):
    image = ImageEnhance.Brightness(image).enhance(1.4)
    image = ImageEnhance.Contrast(image).enhance(1.3)
    image = ImageEnhance.Sharpness(image).enhance(1.5)
    image = image.filter(ImageFilter.GaussianBlur(radius=0.5))
    return image

while True:
    prompt = input("Enter your image prompt: ").strip()

    if prompt.lower() == "q":
        print("Program exited.")
        break

    if not prompt:
        print("Please enter a valid prompt.")
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
            print("Model failed:", e)

    if image is not None:
        print("Applying image enhancements...")

        image = enhance_image(image)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.jpg"

        image.save(filename, quality=95)

        print("Image saved as:", filename)
        image.show()

    else:
        print("Unable to generate the image using the available models.")

    print()