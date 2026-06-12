import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(r'C:\users\shubham\Desktop\ai\lesson 1.cv\m.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

p1 = (100, 100)
p2 = (300, 300)

cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)

cv2.circle(image, p1, 30, (215, 0, 0), -1)

cv2.line(image, p1, p2, (0, 0, 111), 3)

cv2.arrowedLine(image, (400, 50), (400, 300), (56, 85, 0), 4)

cv2.putText(image, f"this my acpppp", (290, 1402), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (85,55,142), 1)

plt.imshow(image)
plt.show()