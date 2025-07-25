"""Server for emotion detector"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyzes text for emotoion
    """
    # Get the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the Emtotion Detector
    response=emotion_detector(text_to_analyze)
    print(response)
    anger=response["anger"]
    disgust=response["disgust"]
    fear=response["fear"]
    joy=response["joy"]
    sadness=response["sadness"]
    dominant_emotion=response["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger' : {anger},
    'disgust' : {disgust}, 'fear' : {fear}, 'joy' : {joy}, and 'sadness' : {sadness}.
    The dominant emotion is {dominant_emotion}"""

@app.route("/")
def render_index_page():
    """
    Renders the page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
