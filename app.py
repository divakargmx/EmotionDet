import os
import cv2
from flask import Flask, render_template, request, jsonify
from deepface import DeepFace

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    data = request.json
    image_data = data['imageData'].split(",")[1]
    
    # Save the uploaded image locally
    image_path = 'uploaded_image.jpg'
    with open(image_path, 'wb') as f:
        f.write(image_data.decode('base64'))

    # Perform FER on the image using deepface
    try:
        emotion_predictions = DeepFace.analyze(image_path, actions=['emotion'])
        emotions = emotion_predictions['emotion']
        top_emotion = max(emotions, key=emotions.get)
        return jsonify({'top_emotion': top_emotion})
    except Exception as e:
        return jsonify({'error': 'Error analyzing emotion.'})

if __name__ == "__main__":
    # Run the Flask app locally using Pywebview
    import webview
    webview.create_window("Emotion Detector", app, width=600, height=400)
    webview.start()
