from auth import *

import requests
import json

access_token = token()



txid = 'jhfdjhfdjh3djhfd4325f6mYw734'




endpoint = f'{url}v2/cob/{txid}'


# payload = "{\r\n  \"calendario\": {\r\n    \"expiracao\": 3600\r\n  },\r\n  \"devedor\": {\r\n    \"cpf\": \"12345678909\",\r\n    \"nome\": \"Gorbadock Oldbuck\"\r\n  },\r\n  \"valor\": {\r\n    \"original\": \"180.50\"\r\n  },\r\n  \"chave\": \"matheus.rodrigues@gerencianet.com.br\",\r\n  \"solicitacaoPagador\": \"Cobrança dos serviços prestados.\"\r\n}"
payload = {
"calendario": {
  "expiracao": 3600 
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



response = requests.request("PUT", endpoint, headers=headers, data = json.dumps(payload), cert=cert)

print(response.text.encode('utf8'))
