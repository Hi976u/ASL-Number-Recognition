from cv2 import cv2, ml_ParamGrid
import time 
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

new_frame_time = 0
prev_frame_time = 0


# path = r'./Screenshot (65).png'
# image = cv2.imread(path)
# window_name = 'image'
# cv2.imshow(window_name, image)
# cv2.resizeWindow("image",650, 400)


cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
wCam, hCam = 800, 1000
cap.set(3, wCam)
cap.set(4, hCam)
with mp_hands.Hands(
  min_detection_confidence=0.75,
  min_tracking_confidence=0.5,
  max_num_hands = 2)as hands:

  while True:
    
    success,image = cap.read()
    if not success :
        print("Skipping Empty Frame!")
        continue

    image = cv2.flip(image,1)

    results = hands.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB)) 

    hand = str(results.multi_handedness)  

    
    
    image.flags.writeable = True
    imageHeight, imageWidth, _ = image.shape

    gesture = "Gesture :-"
    gesture1 = "Gesture :-"
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks :
            mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(16,31,235),thickness=4,circle_radius=0,),
            mp_drawing.DrawingSpec(color=(52,235,135),thickness=2)
            )
            
            normalizedLandmark = hand_landmarks.landmark[4]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Thumb_Tip_x = pixelCoordinatesLandmark[0]
            Thumb_Tip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[6]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Index_Pip_x = pixelCoordinatesLandmark[0]
            Index_Pip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[10]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Middle_Pip_x = pixelCoordinatesLandmark[0]
            Middle_Pip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[14]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Ring_Pip_x = pixelCoordinatesLandmark[0]
            Ring_Pip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[18]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Pinky_Pip_x = pixelCoordinatesLandmark[0]
            Pinky_Pip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[9]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Middle_Mcp_x = pixelCoordinatesLandmark[0]
            Middle_Mcp_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[11]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Middle_Dip_x = pixelCoordinatesLandmark[0]
            Middle_Dip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[15]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Ring_Dip_x = pixelCoordinatesLandmark[0]
            Ring_Dip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[8]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Index_Tip_x = pixelCoordinatesLandmark[0]
            Index_Tip_y = pixelCoordinatesLandmark[1]
            
            normalizedLandmark = hand_landmarks.landmark[2]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Thumb_Mcp_x = pixelCoordinatesLandmark[0]
            Thumb_Mcp_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[5]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Index_Mcp_x = pixelCoordinatesLandmark[0]
            Index_Mcp_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[12]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Middle_Tip_x = pixelCoordinatesLandmark[0]
            Middle_Tip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[16]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Ring_Tip_x = pixelCoordinatesLandmark[0]
            Ring_Tip_y = pixelCoordinatesLandmark[1]

            normalizedLandmark = hand_landmarks.landmark[20]
            pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
            Pinky_Tip_x = pixelCoordinatesLandmark[0]
            Pinky_Tip_y = pixelCoordinatesLandmark[1]
            
            thumb_indx_diff = Thumb_Tip_x-Index_Mcp_x

            if Thumb_Tip_y < Index_Pip_y and Thumb_Tip_y < Middle_Tip_y and Thumb_Tip_y < Ring_Tip_y and Thumb_Tip_y < Pinky_Tip_y:
                gesture = 'Gesture : Zero'
                gesture1 = 'Gesture : 0'

            if Index_Pip_y < Middle_Tip_y and Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y:
                if Index_Tip_y < Middle_Pip_y and Index_Tip_y < Ring_Pip_y and Index_Tip_y < Pinky_Pip_y:
                    gesture = 'Gesture : One'
                    gesture1 = 'Gesture : 1'

            if Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y:
                if Middle_Tip_y < Ring_Pip_y and Middle_Tip_y < Pinky_Pip_y:
                    gesture = 'Gesture : Two'
                    gesture1 = 'Gesture : 2'

            if Index_Pip_y < Pinky_Tip_y and Middle_Pip_y < Pinky_Tip_y and Ring_Pip_y < Pinky_Tip_y :
                if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y:
                    if Index_Tip_y < Thumb_Tip_y and Middle_Tip_y < Thumb_Tip_y and Ring_Tip_y < Thumb_Tip_y:
                         gesture = 'Gesture : Six'
                         gesture1 = 'Gesture : 6'
            
            if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y :
                if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y:
                    gesture = 'Gesture : Four'
                    gesture1 = 'Gesture : 4'

            if Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y and Pinky_Pip_y < Thumb_Tip_y  :
                if  Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Index_Tip_y:
                    gesture = 'Gesture : Nine'  
                    gesture1 = 'Gesture : 9'      
            
            if thumb_indx_diff < -15 :
                if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y:
                    gesture = 'Gesture : Five'
                    gesture1 = 'Gesture : 5'
            

            if thumb_indx_diff < -15 :
                if Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y:
                    if Middle_Tip_y < Ring_Pip_y and Middle_Tip_y < Pinky_Pip_y:
                        gesture = 'Gesture : Three'
                        gesture1 = 'Gesture : 3'

            if Index_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y and Pinky_Pip_y < Thumb_Tip_y :
                if Index_Tip_y < Index_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Middle_Tip_y:
                         gesture = 'Gesture : Eight'
                         gesture1 = 'Gesture : 8'

            if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Pinky_Tip_y < Thumb_Tip_y  :
                if Index_Tip_y < Ring_Tip_y and Middle_Tip_y < Ring_Tip_y and Pinky_Tip_y < Ring_Tip_y :
                    if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Pinky_Tip_y < Pinky_Pip_y:
                         gesture = 'Gesture : Seven'
                         gesture1 = 'Gesture : 7'

            if Thumb_Tip_x < Index_Pip_y and Thumb_Tip_x < Middle_Tip_y and Thumb_Tip_x < Ring_Tip_y and Thumb_Tip_x < Pinky_Tip_y:
                gesture = 'Gesture : Ten'
                gesture1 = 'Gesture : 10'

            
            

    new_frame_time= time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps2text = 'FPS :-'+str(int(fps))


    cv2.rectangle(image,(5,5),(320,130),(0,255,0),-1)
    cv2.rectangle(image,(5,5),(320,130),(0,0,0),3)
    cv2.putText(image,gesture,(20,35),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
    cv2.putText(image,gesture1,(20,75),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
    cv2.putText(image,fps2text,(20,115),cv2.FONT_HERSHEY_COMPLEX,1,(3,3,138),2)

    cv2.imshow('Hand Detection',image)

    if cv2.waitKey(5) & 0xFF == 27 :
        break
    

cv2.destroyAllWindows()        
