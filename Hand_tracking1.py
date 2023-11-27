#2023.07.18 computer vision
#going to test machine learning algorithms- mediapipe

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0) #choose webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#initialize the hand class as store in a variable
mpHands = mp.solutions.hands

#set the hand functin which will hold the landmark points
hands = mpHands.Hands()
#hands = mpHands.Hands(static_image_mode=True,max_num_hands=2, min_num_hands)

#setup the drawing function of hands landmarks on the image
mpDraw = mp.solutions.drawing_utils #drawing utilities

while(cap.isOpened()):#if camera is open
    ret, frame = cap.read()
    if(ret == False):
        break
    if(ret):
        
        fliped_frame = cv2.flip(frame,1)#BGR(mirror image ena nisa cam eka flip kara)
        RGBFrame = cv2.cvtColor(fliped_frame,cv2.COLOR_BGR2RGB)#opencv reads b,g,r format but meadiapipe r,g,b
        results = hands.process(RGBFrame)#RGB
        #print(results)
        #print(results.multi_hand_landmarks) #checking if there have multiple hands

        
        if (results.multi_hand_landmarks):
            for i in range(0,len(results.multi_hand_landmarks)):
                handLms = results.multi_hand_landmarks[i]
                for ilm,lm in enumerate(handLms.landmark):
                    h,w,c = fliped_frame.shape
                    lm_x,lm_y = int(lm.x*w),int(lm.y*h)#w-width, h-height
                    #list_marks.append([i,ilm,lm_x,lm_y])
                    
                #print(list_marks)
                mpDraw.draw_landmarks(fliped_frame, handLms, mpHands.HAND_CONNECTIONS)
        
        cv2.imshow("Frame",fliped_frame) #run a webcam
        
        if(cv2.waitKey(33) & 0xFF == ord('q')):#33mili sec
            cap.release()
            cv2.destroyAllWindows()
            break
    else:
        break

