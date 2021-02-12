import requests
from auth import *
import json

access_token = token()

endpoint = f'{url}v2/pix'

payload = {
    "valor": "00.01",
    "pagador": {
        "chave": "2c5c7441-a91e-4982-8c25-6105581e18ae"
    },
    "favorecido": {
        "chave": "11548080683"
    }
}

headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

response = requests.request("POST", endpoint, headers=headers, data=json.dumps(payload), cert=cert)

print(response.text.encode('utf8'))
