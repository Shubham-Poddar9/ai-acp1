import cv2

image = cv2.imread(r"E:\coding\ai acp\l1.m3\WhatsApp Image 2025-12-19 at 16.39.19.jpeg")

if image is None:
    print("Error: Image not found!")
    exit()

print("Original Shape:", image.shape)

sizes = [(100, 100), (224, 224), (500, 300)]

for size in sizes:
    resized = cv2.resize(image, size)

    window_name = f"Resized Image {size}"
    cv2.imshow(window_name, resized)

    filename = f"resized_{size[0]}x{size[1]}.jpg"
    cv2.imwrite(filename, resized)

    print(f"Saved: {filename}  Shape: {resized.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()