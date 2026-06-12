import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(r'C:\users\shubham\Desktop\ai\lesson 1.cv\m.jpeg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap='gray')
plt.show()

crop = image[200:800, 100:800]   # (y1:y2, x1:x2)
crop_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)

plt.imshow(crop_rgb)
plt.show()

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # 45° rotation
rotated = cv2.warpAffine(image, matrix, (w, h))
rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

plt.imshow(rotated_rgb)
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8") * 80
bright = cv2.add(image, brightness_matrix)
bright_rgb = cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)

plt.imshow(bright_rgb)
plt.show()