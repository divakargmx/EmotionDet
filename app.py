from flask import Flask, request, jsonify
import cv2
from deepface import DeepFace

app = Flask(__name__)

@app.route('/')
def index():
    # Return the index.html file
    return open('index.html').read()

@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    data = request.json
    image_src = data['imageSrc']

    # Perform FER on the image
    # Code for FER (similar to the previous example)

    # For demonstration purposes, we'll return a random emotion as the result
    # Replace this with the actual FER code
    emotions = ['happy', 'sad', 'angry', 'neutral']
    top_emotion = random.choice(emotions)

    return jsonify({'top_emotion': top_emotion})

if __name__ == "__main__":
    app.run()
