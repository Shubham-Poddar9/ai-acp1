from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
from PIL import Image
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(device)

gpt2 = pipeline(
    "text-generation",
    model="gpt2",
    device=0 if device == "cuda" else -1
)

def generate_caption(path):
    image = Image.open(path).convert("RGB")

    inputs = processor(
        images=image,
        return_tensors="pt"
    ).to(device)

    output = model.generate(
        **inputs,
        max_new_tokens=30
    )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption

def expand_caption(caption):
    result = gpt2(
        caption,
        max_new_tokens=50,
        num_return_sequences=1
    )

    return result[0]["generated_text"]

path = input("Enter image path: ")

try:
    caption = generate_caption(path)

    print("\nBasic Caption:")
    print(caption)

    choice = input("\nExpand caption? (yes/no): ")

    if choice.lower() == "yes":
        description = expand_caption(caption)
        print("\nExpanded Caption:")
        print(description)

except Exception as e:
    print("Error:", e)