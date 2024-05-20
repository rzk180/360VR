import requests
import json
import time
from imageGeneration import GetExport

def check_status(id):
  url = "https://backend.blockadelabs.com/api/v1/skybox/export"
  headers = {
    "x-api-key": "{API_KEY}",
    "Content-Type": "application/json"
  }
  data = {
    "skybox_id": id,
    "type_id": "1",
  }
  response = requests.post(url, headers=headers, json=data)
  responseJSON = response.json()

  print(response)

  if responseJSON.get('status') == 'complete':
    return responseJSON.get('id')

  else:
    return "false"
     

def main(id):
  status = "false"
  timeout = 60
  start_time = time.time()
  
  while status == "false": 
    status = check_status(id)
    elapsed_time = time.time() - start_time
    if elapsed_time >= timeout:
      return "error"
    time.sleep(5)
  
  print("PostRequest = DONE\n")
  print(status)
  
  return GetExport.main(status)
