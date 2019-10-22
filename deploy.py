import requests
from requests.auth import HTTPBasicAuth
from proto import prediction_pb2
from proto import prediction_pb2_grpc
import grpc
try:
    from commands import getoutput # python 2
except ImportError:
    from subprocess import getoutput # python 3

API_HTTP="localhost:8002"
API_GRPC="localhost:8003"

def get_token():
    payload = {'grant_type': 'client_credentials'}
    response = requests.post(
                "http://"+API_HTTP+"/oauth/token",
                auth=HTTPBasicAuth('oauth-key', 'oauth-secret'),
                data=payload)
    print(response.text)
    token =  response.json()["access_token"]
    return token

def rest_request():
    token = get_token()
    headers = {'Authorization': 'Bearer '+token}
    payload = {"data":{"names":["sepallengthcm","sepalwidthcm","petallengthcm","petalwidthcm"],"tensor":{"shape":[1,4],"values":[5.1,3.5,1.4,0.2]}}}
    response = requests.post(
                "http://"+API_HTTP+"/api/v0.1/predictions",
                headers=headers,
                json=payload)
    print(response.text)