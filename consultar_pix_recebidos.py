import requests
from auth import *


access_token = token()

data_inicio = '2021-02-10T00:01:35Z'
data_fim = '2021-02-10T23:01:35Z'
txid = '814d97e74d8a4120b94c986dc5c0c356' # parâmetro opcional

endpoint = f'{url}v2/pix?inicio={data_inicio}&fim={data_fim}&txId={txid}''

payload={}

headers = {
  'authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

response = requests.request("GET", endpoint, headers=headers, data=payload, cert=cert)

print(response.text.encode('utf8'))
