import requests
import json 

def main(style_id,text):

  url = "https://backend.blockadelabs.com/api/v1/skybox"
  headers = {
    "x-api-key": "36GshOAMRxms4v8PwRkE1ykBzkaZQecWPOYEcHHGr5unOEibCUfGpBmKoJZM",
    "Content-Type": "application/json"
  }
  data = {
    "prompt": text,
    "negative_text": "negative text example",
    "skybox_style_id": style_id
  }
  response = requests.post(url, headers=headers, json=data)

  return response.text

if __name__ == "__main__":
  response = main(82,"A castle with three trees")
  print(type(response))

