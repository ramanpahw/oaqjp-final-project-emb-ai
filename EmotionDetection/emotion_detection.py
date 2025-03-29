# Library to handle HTTP requests
import requests
# Library to format in Json
import json

def get_parsed_emotion(resp):
    '''
	This function takes as input a text, and returns dictionary of emotions from the response
	'''    
    # Get various scores
    anger_score = resp['emotionPredictions'][0]['emotion']['anger']
    disgust_score = resp['emotionPredictions'][0]['emotion']['disgust']
    fear_score = resp['emotionPredictions'][0]['emotion']['fear']
    joy_score = resp['emotionPredictions'][0]['emotion']['joy']
    sadness_score = resp['emotionPredictions'][0]['emotion']['sadness']
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

def get_dominant_emotion(emotion_dict):
    '''
	This function takes as input a emotion dict, and returns dominant emotion
	'''
    # Get the max key
    emotion_with_max_value = max(emotion_dict, key=emotion_dict.get)
    return emotion_with_max_value

def get_empty_response():
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

# Function: Emotion Detector
def emotion_detector(text_to_analyse):
    '''
	This function takes as input a text_to_analyse, and returns emotion prediction based on the text
	'''
    # URL for the service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Custom header
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Request payload
    obj = { "raw_document": { "text": text_to_analyse } }

    # Sending POST request to the API
    response = requests.post(url, headers = headers, json = obj)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        # Call function to get emotion and scores
        emotion_dict = get_parsed_emotion(formatted_response)

        # Call function to get dominant emotion
        emotion_with_max_value = get_dominant_emotion(emotion_dict)

        # Add the dominant emotion to the dictonary
        emotion_dict['dominant_emotion'] = emotion_with_max_value
    elif response.status_code == 400:
        emotion_dict = get_empty_response()

    # Return JSON
    return emotion_dict
