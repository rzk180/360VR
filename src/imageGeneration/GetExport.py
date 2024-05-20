import requests
from imageGeneration import UploadImageURL

def main(id):
  url = "https://backend.blockadelabs.com/api/v1/skybox/export/" + id
  headers = {
    "x-api-key": "{API_KEY}",
    "Content-Type": "application/json"
  }
  
  response = requests.get(url, headers=headers)
  responseJSON = response.json()

  print("GetExport = DONE\n")
  print(responseJSON.get('file_url'))
  
  return UploadImageURL.main(responseJSON.get('file_url'))

if __name__ == "__main__":
    print()