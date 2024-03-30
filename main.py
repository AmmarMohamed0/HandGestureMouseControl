import cv2
import mediapipe as mp
import pyautogui

video_capture = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_cursor_y = 0

# Calculate conversion factors
width_factor = screen_width / video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height_factor = screen_height / video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

while True:
    _, frame = video_capture.read()
    if frame is None:
        break

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    detection_results = hand_detector.process(rgb_frame)
    detected_hands = detection_results.multi_hand_landmarks

    if detected_hands:
        for hand_landmarks in detected_hands:
            drawing_utils.draw_landmarks(frame, hand_landmarks)
            landmarks = hand_landmarks.landmark

            for landmark_id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if landmark_id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_cursor_x = width_factor * x
                    index_cursor_y = height_factor * y
                    # Adjust the duration parameter to change mouse movement speed
                    move_duration = 0.01  # Adjust as needed
                    pyautogui.moveTo(index_cursor_x, index_cursor_y, duration=move_duration)

                if landmark_id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = width_factor * x
                    thumb_y = height_factor * y
                    thumb_index_distance = abs(index_cursor_y - thumb_y)

                    if thumb_index_distance < 20:
                        print('Distance between thumb and index finger:', thumb_index_distance)
                        print('Click detected')
                        pyautogui.click()
                        pyautogui.sleep(0.2)

    cv2.imshow('virtual image', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
