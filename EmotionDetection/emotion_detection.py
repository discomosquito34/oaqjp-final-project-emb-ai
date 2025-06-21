import requests
import json
def emotion_detector(text_to_analyze): 
    url="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonObject={ "raw_document": { "text": text_to_analyze } }
    response= requests.post(url, json=jsonObject, headers=header)
    print(response.status_code)
    #Create the dictionary with all required data
    if response.status_code == 400: 
        formatted_dict={
            "anger":None, 
            "disgust":None, 
            "fear":None, 
            "joy":None, 
            "sadness":None, 
            "dominant_emotion":None
            }
    else: 
        #Get the dictionary
        new_dictionary=json.loads(response.text)

        #Get the relevant sub dictionary 
        emotions=new_dictionary["emotionPredictions"][0]["emotion"]

        #Find the dominant emotion
        dominant_emotion=max(emotions, key=emotions.get)
        formatted_dict={
                "anger":emotions["anger"], 
                "disgust":emotions["disgust"], 
                "fear":emotions["fear"], 
                "joy":emotions["joy"], 
                "sadness":emotions["sadness"], 
                "dominant_emotion":dominant_emotion
                }
    return formatted_dict

