# HandGestureMouseControl

- Import necessary libraries:
  - `cv2`: OpenCV library for computer vision tasks.
  - `mediapipe`: A framework developed by Google for building multimodal (such as hands, face, pose) applied machine learning pipelines.
  - `pyautogui`: A library to control the mouse and keyboard to automate interactions with the GUI.

- Set up the video capture from the default webcam (`VideoCapture(0)`).

- Initialize the hand detection model (`Hand` class) from the `mediapipe.solutions.hands` module.

- Define some variables:
  - `drawing_utils`: Utilities for drawing landmarks detected by Mediapipe on the frame.
  - `screen_width` and `screen_height`: Obtain the screen size using `pyautogui.size()` for mapping hand gestures to the screen.
  - `index_cursor_y`: Initialize the y-coordinate of the cursor controlled by the index finger.

- Inside the main loop:
  - Read frames from the webcam.
  - Flip the frame horizontally to match the user's perspective.
  - Convert the frame from BGR to RGB color space (required by Mediapipe).
  - Detect hands using the `hand_detector` initialized earlier.
  - If hands are detected, iterate over each detected hand:
    - Draw landmarks on the frame using `drawing_utils.draw_landmarks`.
    - Extract landmarks' coordinates and perform actions based on specific landmarks (e.g., thumb and index finger).
    - Calculate cursor positions based on hand landmarks and screen dimensions.
    - Move the cursor using `pyautogui.moveTo`.
    - Simulate a mouse click if the thumb and index finger are close together using `pyautogui.click`.

- Display the processed frame with the detected landmarks.

- Wait for the user to press 'q' to quit the program.

- Release the video capture and close all OpenCV windows.

## Contributing:
Contributions to HandGestureMouseControl are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgements:
- OpenCV: [https://opencv.org/](https://opencv.org/)
- Mediapipe: [https://mediapipe.dev/](https://mediapipe.dev/)
- PyAutoGUI: [https://pyautogui.readthedocs.io/](https://pyautogui.readthedocs.io/)
