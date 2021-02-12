import requests
from auth import *
import json


access_token = token()

chave = '2c5c7441-a91e-4982-8c25-6105581e18ae'
endpoint = f'{url}v2/webhook/{chave}'

payload={}
headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", endpoint, headers=headers, data=json.dumps(payload), cert=cert)

print(response.text.encode('utf8'))