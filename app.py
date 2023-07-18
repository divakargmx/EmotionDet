import webview
import cv2
from deepface import DeepFace

def process_image(image_path):
    # Load the image and convert it to grayscale
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If a face is detected, perform emotion recognition
    if len(faces) > 0:
        emotion_predictions = DeepFace.analyze(image_path, actions=['emotion'])
        emotions = emotion_predictions['emotion']
        top_emotion = max(emotions, key=emotions.get)
        print("Top Emotion:", top_emotion)
    else:
        print("No face detected in the image.")

def create_window():
    webview.create_window("Image Uploader and Viewer", "index.html", width=600, height=400, js_api=process_image)

if __name__ == "__main__":
    create_window()
