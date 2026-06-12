import cv2
import numpy as np
import matplotlib.pyplot as plt 

def show(title, img):
    plt.imshow(img, cmap="gray")
    plt.title(title)
    plt.show()

def image_app(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    while True:
        print("MENU")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Gaussian Blur")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
            sobel = cv2.bitwise_or(
                np.uint8(np.absolute(sobelx)),
                np.uint8(np.absolute(sobely))
            )
            show("Sobel Edge", sobel)

        elif choice == "2":
            low = int(input("Enter low threshold: "))
            high = int(input("Enter high threshold: "))
            edges = cv2.Canny(gray, low, high)
            show("Canny Edge", edges)

        elif choice == "3":
            k = int(input("Enter kernel size (odd number): "))
            blur = cv2.GaussianBlur(gray, (k, k), 0)
            show("Gaussian Blur", blur)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

image_app(r"C:\Users\shubham\Desktop\ai\lesson 1.cv\m.jpeg")