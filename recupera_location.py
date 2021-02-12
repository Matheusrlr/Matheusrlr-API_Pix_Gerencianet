from auth import *

import requests
import json

access_token = token()

id = '255'


endpoint = f'{url}v2/loc/{id}'


payload = {}


headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}



response = requests.request("GET", endpoint, headers=headers, data=payload, cert=cert)

print(response.text.encode('utf8'))
