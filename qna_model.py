import requests
import json

def query(API_URL, headers, payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def bertModel(configfile, question, context):
    f = open(configfile)
    api_config = json.load(f)
    API_TOKEN = api_config['API_TOKEN']
    API_URL = "https://api-inference.huggingface.co/models/bert-large-uncased-whole-word-masking-finetuned-squad"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {
        "inputs": {
            "question": str(question),
            "context": str(context)
        },
    }

    output = query(API_URL, headers, payload)
    return output