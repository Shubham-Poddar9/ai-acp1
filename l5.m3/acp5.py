import cv2, time, pyautogui, mediapipe as mp
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
draw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)

SCROLL,DELAY=300,1
last=p=0

def gesture(hand,side):
    tips=[8,12,16,20]
    f=sum(hand.landmark[t].y<hand.landmark[t-2].y for t in tips)

    thumb=hand.landmark[4].x
    joint=hand.landmark[3].x
    if(side=='Right'and thumb>joint)or(side=='Left'and thumb<joint):
        f += 1

    return "up" if f==5 else "down" if f ==0 else "none"
while cap.isOpened():
    ok, img = cap.read()
    if not ok:
        break

    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    g="none"

    if result.multi_hand_landmarks:
        hand=result.multi_hand_landmarks[0]
        side=result.multi_handedness[0].classification[0].label

        g=gesture(hand,side)

        draw.draw_landmarks(img,hand,mp_hands.HAND_CONNECTIONS)

        if time.time()-last>DELAY:
            if g=="up":
                pyautogui.scroll(SCROLL)

            elif g=="down":
                pyautogui.scroll(-SCROLL)
            last=time.time()

    
    cv2.putText(img,g.upper(),(20,40),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(255,0,0),2)

    cv2.imshow("gesture control",img)

    if cv2.waitKey(1) &0xFF== ord("q"):
        break


cap.release()
cv2.destroyAllWindows()