from auth import *

import requests
import json

access_token = token()

e2eid = 'E18236120202101172323s08267214CO'

ID = 'd553213f3561483ed'


endpoint = f'{url}v2/pix/{e2eid}/devolucao/{ID}'



payload = {
  "valor": "0.01" 
}



headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}


response = requests.request("PUT", endpoint, headers=headers, data=json.dumps(payload), cert=cert)

print(response.text.encode('utf8'))
