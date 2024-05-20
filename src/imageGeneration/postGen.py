import requests
from imageGeneration import PostRequestExport

def main(style_id,text):

  url = "https://backend.blockadelabs.com/api/v1/skybox"
  headers = {
    "x-api-key": "36GshOAMRxms4v8PwRkE1ykBzkaZQecWPOYEcHHGr5unOEibCUfGpBmKoJZM",
    "Content-Type": "application/json"
  }
  data = {
    "prompt": str(text),
    "negative_text": "negative text example",
    "skybox_style_id": int(style_id)
  }
  response = requests.post(url, headers=headers, json=data)
  responseJSON = response.json()

  print("PostGen = DONE \n")
  print(responseJSON)

  return PostRequestExport.main(responseJSON.get('obfuscated_id'))

if __name__ == "__main__":
  response = main(3,"A dog looking cool on his jetski")
  print(response.get('obfuscated_id'))