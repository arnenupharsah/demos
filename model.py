import requests
import json


def send_search(search_text):
    params = {'search_text':search_text} 
    #requests.post(url1, data=json.dumps(params))
    return json.dumps(params)
    