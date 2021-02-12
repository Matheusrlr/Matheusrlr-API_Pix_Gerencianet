import requests
from auth import *
import json


access_token = token()


data_inicio = '2021-01-14T16:01:35Z'
data_fim = '2021-01-18T16:01:35Z'

endpoint = f'{url}v2/webhook/?inicio={data_inicio}&fim={data_fim}'


payload={}
headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

response = requests.request("GET", endpoint, headers=headers, data=payload, cert=cert)

print(response.text.encode('utf8'))