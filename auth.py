from credentials import *
import requests
import base64

if (sandbox == True):
        url = "https://api-pix.gerencianet.com.br/"
else: url = "https://api-pix-h.gerencianet.com.br/" 

credentials = {
    "client_id": client_id,
    "client_secret": client_secret,
}
cert = f'certificados\{certificado}'

auth = base64.b64encode(
    (f"{credentials['client_id']}:{credentials['client_secret']}"
     ).encode()).decode()

def token():

  endpoint = f"{url}oauth/token"

  payload = "{\r\n    \"grant_type\": \"client_credentials\"\r\n}"
  headers = {

    'Authorization': f"Basic {auth}",
    'Content-Type': 'application/json'
  }

      
  response = requests.request("POST", endpoint, headers=headers, data = payload , cert= cert)
  result = response.json().get('access_token')
  return result



