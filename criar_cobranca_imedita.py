from auth import *

import requests
import json

access_token = token()



endpoint = f'{url}v2/cob/'


payload = {
"calendario": {
  "expiracao": 3600 
  },
"devedor": {
  "cpf": "12345678909",
  "nome": "Gorbadock Oldbuck"
  },
"valor": {
  "original": "0.01"
  },
"chave": "",
"solicitacaoPagador": "Cobrança dos serviços prestados."}



headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}



response = requests.request("POST", endpoint, headers=headers, data=json.dumps(payload), cert=cert)

print(response.text.encode('utf8'))
