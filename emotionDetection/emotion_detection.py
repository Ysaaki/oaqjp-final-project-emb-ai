import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the Watson NLP Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Construct the input JSON payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Check for a 400 bad request status code (e.g., blank text input)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    # If the response status code is 200 (OK), parse and extract scores normally
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract individual emotion scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Logic to find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Construct the desired output dictionary format
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result