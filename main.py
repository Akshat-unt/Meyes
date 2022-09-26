"""
A script to control your cursor with your eyes
"""

import cv2  # OpenCV
import mediapipe as mp  # Google's MediaPipe
import pyautogui  # PyAutoGUI


cam = cv2.VideoCapture(0)  # 0 for internal webcam, 1 for external webcam
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)  # FaceMesh
screen_w, screen_h = pyautogui.size()  # Screen size
while True:
    _, frame = cam.read()  # Read the frame
    frame = cv2.flip(frame, 1)  # Flip the frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
    output = face_mesh.process(rgb_frame)  # Process the frame
    landmark_points = output.multi_face_landmarks  # Landmark points
    frame_h, frame_w, _ = frame.shape  # Frame size

    if landmark_points:  # If there are landmark points
        landmarks = landmark_points[0].landmark  # Landmarks
        for i, landmark in enumerate(landmarks[474:478]):  # For each landmark
            x = int(landmark.x * frame_w)  # X coordinate
            y = int(landmark.y * frame_h)  # Y coordinate
            cv2.circle(frame, (x, y), 3, (0, 255, 0))  # Draw a circle

            if i == 1:  # If the landmark is the right eye
                screen_x = screen_w * landmark.x  # X coordinate
                screen_y = screen_h * landmark.y  # Y coordinate
                pyautogui.moveTo(screen_x, screen_y)  # Move the cursor

        left = [landmarks[145], landmarks[159]]  # Left eye
        for landmark in left:  # For each landmark
            x = int(landmark.x * frame_w)  # X coordinate
            y = int(landmark.y * frame_h)  # Y coordinate
            cv2.circle(frame, (x, y), 3, (0, 255, 255))  # Draw a circle

        if (left[0].y - left[1].y) < 0.004:  # If the left eye is closed
            pyautogui.click()  # Click
            pyautogui.sleep(1)  # Wait for 1 second

    cv2.imshow("Meyes ", frame)  # Show the frame
    cv2.waitKey(1)  # Wait for 1 millisecond
