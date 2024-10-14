import json
import requests

POST_PHONE = "https://afishauz-backend.uz/api/mobile/delete-account"
POST_CODE = "https://afishauz-backend.uz/api/mobile/confirm-delete-sms"

def post_number(lang:str, number:str) -> list:
    response = requests.post(POST_PHONE, headers={"Accept-Language":lang}, data={'phone':number})
    return [response.json()['status'], response.json()['message']]

def post_code(lang:str, number:str, code:str) -> str:
    response = requests.post(POST_CODE, headers={"Accept-Language":lang}, data={'phone':number, 'code':code})
    return [response.json()['status'], response.json()['message']]
