import requests

def emotion_detector(text_to_analyze):
    # Define Watson API endpoint and headers
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Construct the payload to send to Watson
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        # Send a POST request to the Watson API
        response = requests.post(url, json=payload, headers=headers)
        
        # Raise an error if the response is unsuccessful. status code 200 if success
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()

        # Extract the "emotion" field from the response
        emotions = data["emotionPredictions"][0]["emotion"]
        
        # Return only the relevant emotions and their scores
        return emotions

    except requests.exceptions.RequestException as e:
        # Return an error message if something goes wrong
        return f"An error occurred: {e}"
