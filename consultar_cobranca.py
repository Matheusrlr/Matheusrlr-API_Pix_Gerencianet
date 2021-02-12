import requests
from auth import *

access_token = token()

txid = '7a95bc659cd54e6b9cedba8189bbad15'

endpoint = f'{url}v2/cob/{txid}'

payload={}

headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

response = requests.request("GET", endpoint, headers=headers, data=payload, cert=cert)

print(response.text.encode('utf8'))
