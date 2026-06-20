import cv2

def color_filter(img, f):
    if f == "red":
        img[:, :, 0] = 0
        img[:, :, 1] = 0

    elif f == "cyan":
        img[:, :, 2] = 0   

    elif f == "pink":
        img[:, :, 0] = 0  

    elif f == "purple":
        img[:, :, 1] = 0  

    elif f == "original":
        pass

    return img   


cap = cv2.VideoCapture(0)
f = "original"

print("r for red, c for cyan, p for pink, z for purple, o for original, q for quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    filtered = color_filter(frame.copy(), f)
    cv2.imshow("filters", filtered)

    k = cv2.waitKey(1) & 0xFF

    if k == ord("r"):
        f = "red"
    elif k == ord("c"):
        f = "cyan"
    elif k == ord("p"):
        f = "pink"
    elif k == ord("z"):
        f = "purple"
    elif k == ord("o"):
        f = "original"
    elif k == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()