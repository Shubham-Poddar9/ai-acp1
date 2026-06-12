import cv2

img = cv2.imread(r"C:\Users\shubham\Desktop\ai\lesson 1.cv\m.jpeg")

if img is None:
    print("error")
else:
    print("r = red tint")
    print("g = green tint")
    print("b = blue tint")
    print("i = increase red")
    print("k = decrease red")
    print("o = increase green")
    print("l = decrease green")
    print("p = increase blue")
    print("m = decrease blue")
    print("q = quit")

    new_img = img.copy()

    while True:
        cv2.imshow("filtered image", new_img)
        key = cv2.waitKey(0)

        if key == ord("r"):
            new_img[:,:,0] = 0
            new_img[:,:,1] = 0

        elif key == ord("g"):
            new_img[:,:,0] = 0
            new_img[:,:,2] = 0

        elif key == ord("b"):
            new_img[:,:,1] = 0
            new_img[:,:,2] = 0

        # increase / decrease channels
        elif key == ord("i"):
            new_img[:,:,2] = cv2.add(new_img[:,:,2], 30)

        elif key == ord("k"):
            new_img[:,:,2] = cv2.subtract(new_img[:,:,2], 30)

        elif key == ord("o"):
            new_img[:,:,1] = cv2.add(new_img[:,:,1], 30)

        elif key == ord("l"):
            new_img[:,:,1] = cv2.subtract(new_img[:,:,1], 30)

        elif key == ord("p"):
            new_img[:,:,0] = cv2.add(new_img[:,:,0], 30)

        elif key == ord("m"):
            new_img[:,:,0] = cv2.subtract(new_img[:,:,0], 30)

        elif key == ord("q"):
            break

cv2.destroyAllWindows()