# Library to handle HTTP requests
import requests

# Function: Emotion Detector
def emotion_detector(text_to_analyse):
    '''
	This function takes as input a text_to_analyse, and returns emotion prediction based on the text
	'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers = headers, json = obj)
    return response.text
