"""
Server module for the Emotion Detection application.
Provides endpoints to render the web interface and analyze text input
using the EmotionDetection package built over Watson NLP.
"""
from flask import Flask, render_template, request
from emotionDetection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Retrieves text from request arguments, parses emotions using the
    packaged emotion_detector tool, and formats a human-readable string response.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Run the emotion detection function on the text
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None (indicating an empty/invalid entry)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response into the exact string requested by the client
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_response


@app.route("/")
def render_index_page():
    """
    Renders the default landing page template interface.
    """
    return render_template('index.html')


if __name__ == "__main__":
    # Host the application on localhost at port 5000
    app.run(host="0.0.0.0", port=5000)