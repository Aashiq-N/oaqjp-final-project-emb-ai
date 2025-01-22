from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Route to serve the HTML interface
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle emotion detection
@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    # Get the input text from the query parameter
    input_text = request.args.get('textToAnalyze', '')

    # Handle blank or invalid input
    if not input_text.strip():
        print("Invalid text! Please try again!")  # Output to the terminal
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Call the emotion_detector function
    result = emotion_detector(input_text)

    # Handle None values in the result
    if result["dominant_emotion"] is None:
        print("Invalid text! Please try again!")  # Output to the terminal
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Format the response
    response = {
        "message": f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    }
    print(response["message"])  # Output valid responses to the terminal
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
