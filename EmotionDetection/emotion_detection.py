import requests

def emotion_detector(text_to_analyze):
    # Define Watson API endpoint and headers
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Handle blank or invalid input
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Construct the payload to send to Watson
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        # Send a POST request to the Watson API
        response = requests.post(url, json=payload, headers=headers)
        
        # Handle unsuccessful status codes
        if response.status_code != 200:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
        
        # Parse the JSON response
        data = response.json()

        # Extract the "emotion" field from the response
        emotions = data["emotionPredictions"][0]["emotion"]

        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = dominant_emotion

        # Return the parsed emotions
        return emotions

    except requests.exceptions.RequestException:
        # Return None for all values in case of an exception
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
