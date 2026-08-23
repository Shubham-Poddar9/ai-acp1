from huggingface_hub import InferenceClient
from datetime import datetime


models = [
    "ByteDance/SDXL-Lightning",
    "stabilityai/stable-diffusion-xl-base-1.0",
    "stabilityai/sdxl-turbo",
    "runwayml/stable-diffusion-v1-5"
]


api = ""

client = InferenceClient(api_key=api)

print("Primary model:", models[0])
print("Type 'q' to exit")


styles = {
    "1": "photorealistic, highly detailed, cinematic lighting",
    "2": "digital art, vibrant colors, detailed illustration",
    "3": "anime style, clean lines, colorful, detailed",
    "4": "oil painting, artistic brush strokes, classical style",
    "5": "3D render, realistic materials, studio lighting"
}

while True:

    prompt = input("\nEnter your prompt: ").strip()

    if prompt.lower() == "q":
        print("Exiting...")
        break

    if not prompt:
        print("Please enter a prompt.")
        continue

    print("\nChoose a style:")
    for key, value in styles.items():
        print(f"{key}. {value}")

    style_choice = input("Enter style number: ").strip()

    style = styles.get(
        style_choice,
        "high quality, detailed"
    )

    negative_prompt = input(
        "Enter negative prompt (press Enter to skip): "
    ).strip()

    try:
        steps = int(input("Inference steps (10-50): ") or 25)
        guidance = float(
            input("Guidance scale (1-15): ") or 7.5
        )
    except ValueError:
        print("Invalid value. Using default settings.")
        steps = 25
        guidance = 7.5

    final_prompt = f"{prompt}, {style}"

    print("\nGenerating image...")
    print("Prompt:", final_prompt)

    image = None

    for model in models:

        try:
            print("Trying model:", model)

            # Additional parameters give more control
            image = client.text_to_image(
                prompt=final_prompt,
                model=model,
                negative_prompt=negative_prompt,
                num_inference_steps=steps,
                guidance_scale=guidance
            )

            print("Model used:", model)
            break

        except Exception as e:
            print("Error with", model)
            print(e)
            continue

    if image:

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = f"generated_{timestamp}.png"

        image.save(filename)

        print("\nImage generated successfully!")
        print("Saved as:", filename)

        image.show()

    else:
        print("\nUnable to generate the image.")
        print("Please try another prompt or model.")