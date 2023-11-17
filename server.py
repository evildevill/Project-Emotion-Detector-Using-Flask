"""
Emotion Detection Server

This script, server.py, is the main entry point for our application. 
It sets up a server using the Flask framework, a lightweight and flexible 
micro web framework for Python.

The server is designed to perform emotion detection on user-provided text. 
Emotion detection, or sentiment analysis, is a field of Natural Language 
Processing (NLP) that involves determining the emotional tone behind words. 
This can be useful in a variety of applications, such as analyzing customer feedback, 
social media monitoring, and many more.

The server receives text input from the user, processes it, and returns an emotion 
classification. The classifications could be, for example, 'happy', 'sad', 'angry', etc., 
depending on the implementation of the emotion detection algorithm.

The server is designed to handle multiple requests concurrently and is capable of scaling to 
handle increased load, making it suitable for real-world applications.

Author: Waseem Akram (https://github.com/evildevill/)
"""
 
from flask import Flask, render_template, request, jsonify

from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection Web App Using Flask")

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_detect = request.args.get('textToAnalyze')
    
    if not text_to_detect:
        return jsonify({'error': 'Invalid request. Please provide textToAnalyze parameter.'}), 400

    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)

    if formated_response['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again.'}), 500

    return jsonify({
        'anger': formated_response['anger'],
        'disgust': formated_response['disgust'],
        'fear': formated_response['fear'],
        'joy': formated_response['joy'],
        'sadness': formated_response['sadness'],
        'dominant_emotion': formated_response['dominant_emotion']
    })

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == "__main__":
    run_emotion_detection()
