from auth import *

import requests
import json

access_token = token()



endpoint = f'{url}v2/loc'



payload = {
  "tipoCob": "cob" 
}



headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}


response = requests.request("POST", endpoint, headers=headers, data=json.dumps(payload), cert=cert)

print(response.text.encode('utf8'))
