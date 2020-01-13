import requests
import random
import json
import time


url = "https://apiv2.favoriot.com/v2/streams"

def streamData(device_developer_id,accesstoken): 

  params = {
    'device_developer_id' : device_developer_id,
    'data':{
      'temperature':random.randint(0,100), 
      'humidity':random.randint(0,100)
    }
  }
  headers = {
      'accesstoken': accesstoken,
      'content-type': "application/json",
      'cache-control': "no-cache",
     }
 
  respons = requests.post(url, data=json.dumps(params), headers=headers)
  print respons.text


if __name__ == '__main__':
    device_developer_id = '' # put your device_developer_id
    accesstoken = '' # put your access token 
    while True:
      streamData(device_developer_id,accesstoken)
      time.sleep(10)