import cv2,time,numpy as np,mediapipe as mp

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
draw=mp.solutions.drawing_utils

cap=cv2.VideoCapture(0)

filters=["grayscale","sepia","negative","blur"]
f=0
last=0

while True:
    ret,img=cap.read()
    if not ret:
        break

    img=cv2.flip(img,1)
    h,w=img.shape[:2]

    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result=hands.process(rgb)

    if result.multi_hand_landmarks:
        hand=result.multi_hand_landmarks[0]
        draw.draw_landmarks(img,hand,mp_hands.HAND_CONNECTIONS)

        lm=hand.landmark

        thumb=(int(lm[4].x*w),int(lm[4].y*h))
        index=(int(lm[8].x*w),int(lm[8].y*h))
        middle=(int(lm[12].x*w),int(lm[12].y*h))

        if abs(thumb[0]-index[0])<20 and abs(thumb[1]-index[1])<20:
            if time.time()-last>1:
                cv2.imwrite(f"photo_{int(time.time())}.jpg",img)
                last=time.time()

        elif abs(thumb[0]-middle[0])<20 and abs(thumb[1]-middle[1])<20:
            if time.time()-last>1:
                f=(f+1)%len(filters)
                last=time.time()

    frame=img.copy()

    if filters[f]=="grayscale":
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        frame=cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

    elif filters[f]=="sepia":
        kernel=np.array([[0.272,0.534,0.131],
                         [0.349,0.686,0.168],
                         [0.393,0.769,0.189]])
        frame=cv2.transform(frame,kernel)
        frame=np.clip(frame,0,255).astype(np.uint8)

    elif filters[f]=="negative":
        frame=cv2.bitwise_not(frame)

    elif filters[f]=="blur":
        frame=cv2.GaussianBlur(frame,(15,15),0)

    cv2.putText(frame,filters[f],(20,40),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),2)

    cv2.imshow("Gesture Camera",frame)

    if cv2.waitKey(1)&0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()