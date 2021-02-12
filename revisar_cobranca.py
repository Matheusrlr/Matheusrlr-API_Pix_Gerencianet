from auth import *

import requests
import json

access_token = token()


txid = 'fb8065d3ca4c4045bf1e80556261a043'
endpoint = f'{url}v2/cob/+txid'


payload = {

"loc": {
"id": 260
},  
"calendario": {
  "expiracao": 9000 
  },
"devedor": {
  "cpf": "12345678909",
  "nome": "Gorbadock Oldbuck"
  },
"valor": {
  "original": "1.50"
  },
"chave": "matheus.rodrigues@gerencianet.com.br",
"solicitacaoPagador": "Cobrança dos serviços prestados."}



headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

payload = json.dumps(payload)

response = requests.request("PATCH", endpoint, headers=headers, data=payload, cert=cert)

print(response.text.encode('utf8'))
