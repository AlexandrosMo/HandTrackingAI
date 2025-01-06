import cv2

class FaceIDDetection:
    """
    A class to perform face detection and recognize faces using OpenCV.
    
    Attributes:
        face_cascade (cv2.CascadeClassifier): Haar cascade classifier for face detection.
        webcam (cv2.VideoCapture): Webcam object to capture video frames.
    """
    
    def __init__(self, cascade_path='haarcascade_frontalface_default.xml'):
        """
        Initializes the FaceIDDetection class with a webcam feed and a pre-trained Haar Cascade classifier.

        Parameters:
            cascade_path (str): The path to the Haar Cascade XML file for face detection (default: 'haarcascade_frontalface_default.xml').
        """
        # Load the pre-trained Haar Cascade model for face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)
        
        # Initialize the webcam feed (camera index 0 is typically the default webcam)
        self.webcam = cv2.VideoCapture(0)
        
        if not self.webcam.isOpened():
            print("Error: Camera could not be accessed.")
            raise Exception("Camera initialization failed.")
        
    def detect_faces(self, frame):
        """
        Detects faces in the given frame using Haar cascade classifier.

        Parameters:
            frame (ndarray): The image frame in which faces need to be detected.
        
        Returns:
            faces (list of tuples): A list of rectangles where faces are detected, each tuple contains (x, y, w, h).
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        return faces

    def display_faces(self, frame, faces):
        """
        Draws rectangles around detected faces and displays the result.

        Parameters:
            frame (ndarray): The image frame in which faces are detected.
            faces (list of tuples): A list of rectangles where faces are detected.
        """
        for (x, y, w, h) in faces:
            # Draw rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Show the output frame with detected faces
        cv2.imshow('Face Detection', frame)
    
    def start_detection(self):
        """
        Starts the webcam feed and performs real-time face detection.
        The webcam feed continues until the user presses 'q' to quit.
        """
        while True:
            ret, frame = self.webcam.read()  # Read a frame from the webcam
            if not ret:
                print("Error: Failed to grab frame.")
                break

            # Detect faces in the current frame
            faces = self.detect_faces(frame)

            # Display the faces on the frame
            self.display_faces(frame, faces)

            # Wait for key press and break if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release the webcam and close all OpenCV windows
        self.webcam.release()
        cv2.destroyAllWindows()

    def save_face_image(self, frame, faces):
        """
        Saves the first detected face as an image file.
        
        Parameters:
            frame (ndarray): The image frame where faces are detected.
            faces (list of tuples): A list of rectangles where faces are detected.
        """
        if len(faces) > 0:
            # Crop the first detected face from the frame
            (x, y, w, h) = faces[0]
            face = frame[y:y+h, x:x+w]

            # Save the detected face as an image
            cv2.imwrite('detected_face.jpg', face)
            print("Face image saved as 'detected_face.jpg'.")
        else:
            print("No face detected to save.")
    
    def close(self):
        """
        Releases the webcam and closes any open OpenCV windows.
        """
        self.webcam.release()
        cv2.destroyAllWindows()

# Example usage:
if __name__ == "__main__":
    # Create an instance of the FaceIDDetection class
    face_id_detector = FaceIDDetection()

    try:
        # Start real-time face detection
        face_id_detector.start_detection()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure proper cleanup
        face_id_detector.close()
