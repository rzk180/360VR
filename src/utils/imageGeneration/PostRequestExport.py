import requests

def main():
  url = "https://backend.blockadelabs.com/api/v1/skybox/export"

  payload = "{\n    \"skybox_id\": \"dd03ab3e576ec65f0f805ff3695e0d61\",\n    \"type_id\": 1\n}"
  headers = {
    'x-api-key': '36GshOAMRxms4v8PwRkE1ykBzkaZQecWPOYEcHHGr5unOEibCUfGpBmKoJZM'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return response.text

if __name__ == "__main__":
    response = main(id)