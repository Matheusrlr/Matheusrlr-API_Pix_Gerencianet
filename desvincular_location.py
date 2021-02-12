from auth import *

import requests
import json

access_token = token()

id = '255'
txid = 'f76833fe4f1e48d5af53a2413d55c8cb'

endpoint = f'{url}v2/loc/{id}/{txid}'


payload = {}


headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}



response = requests.request("DELETE", endpoint, headers=headers, data=payload, cert=cert)

print(response.text.encode('utf8'))
