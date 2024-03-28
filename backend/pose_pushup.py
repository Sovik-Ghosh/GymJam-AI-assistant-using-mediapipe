import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm

def pushup():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    direction = 0
    form = 0
    feedback = "LOWER YOUR WAIST"

    with detector.pose:
        while True:
                
            ret, img = cap.read() #640 x 480


            img = detector.findPose(img, False)
            lmList = detector.findPosition(img, False)
            # print(lmList)
            if len(lmList) != 0:
                elbow = detector.findAngle(img, 11, 13, 15)
                shoulder = detector.findAngle(img, 13, 11, 23)
                hip = detector.findAngle(img, 11, 23,25)
                
                #Percentage of success of pushup
                per = np.interp(elbow, (90, 160), (0, 100))
                
                #Bar to show Pushup progress
                bar = np.interp(elbow, (90, 160), (380, 50))

                #Check to ensure right form before starting the program
                if elbow > 160 and shoulder > 40 and hip > 160:
                    form = 1
            
                #Check for full range of motion for the pushup
                if form == 1:
                    if per == 0:
                        if elbow <= 90 and hip > 160:
                            feedback = "UP"
                            if direction == 0:
                                count += 0.5
                                direction = 1
                        else:
                            feedback = "LOWER YOUR WAIST"
                            
                    if per == 100:
                        if elbow > 160 and shoulder > 40 and hip > 160:
                            feedback = "DOWN"
                            if direction == 1:
                                count += 0.5
                                direction = 0
                        else:
                            feedback = "LOWER YOUR WAIST"
                                # form = 0

                print(count)
                
                #Draw Bar
                if form == 1:
                    cv2.rectangle(img, (1080, 50), (1100, 380), (0, 255, 0), 3)
                    cv2.rectangle(img, (1080, int(bar)), (1100, 380), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, f'{int(per)}%', (950, 230), cv2.FONT_HERSHEY_PLAIN, 2,
                                (255, 255, 0), 2)


                #Pushup counter
                cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                            (255, 0, 0), 5)
                
                #Feedback 
                
                cv2.putText(img, feedback, (500, 40 ), cv2.FONT_HERSHEY_PLAIN, 2,
                            (255, 255, 0), 2)

                
            # Convert the frame to JPEG format
                ret, jpeg = cv2.imencode('.jpg', img)

                # Yield the frame as a bytes-like object
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')