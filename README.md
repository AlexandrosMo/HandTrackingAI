Hand Tracking AI with OpenCV and MediaPipe

This project demonstrates real-time hand tracking using OpenCV and MediaPipe. It captures video through a webcam to track hand landmarks, highlights the first landmark with a circle, and displays the frames per second (FPS) for performance monitoring. The application is built for Windows but can be easily adapted to other operating systems.

Features:
Real-time hand detection using MediaPipe's hand tracking model.
Displays hand landmarks and connections for the detected hand.
Calculates and displays FPS for performance feedback.
Allows users to stop the program by pressing 'q' or 'ESC'.
Requirements:
Python 3.x
OpenCV
MediaPipe
Installation:
Clone the repository or download the project files.

Create a virtual environment (recommended) and activate it:
python -m venv venv
venv\Scripts\activate 

Install the required packages:
pip install opencv-python mediapipe

Run the Python script:
python HandsTrackingAI.py

How It Works:
The program starts by initializing the camera using OpenCV’s cv2.VideoCapture(0) function.
Frames captured from the camera are processed using MediaPipe's hand tracking model.
The program detects the landmarks of the hand and prints the coordinates for each.
The processed image is displayed with landmarks, with a circle drawn on the first landmark.
The FPS (frames per second) is calculated and displayed for performance monitoring.
Press 'q' or 'ESC' to close the application.
This hand tracking AI application provides a simple and effective way to detect and monitor hand movements in real-time. 

(Web Camera Needed)
