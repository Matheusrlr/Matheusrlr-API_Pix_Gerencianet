from auth import *

import requests
import json

access_token = token()

e2eid = 'E18236120202101172323s08267214CO'


endpoint = f'{url}v2/pix/{e2eid}'


payload = {}


headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}



response = requests.request("GET", endpoint, headers=headers, data=payload, cert=cert)

print(response.text.encode('utf8'))
