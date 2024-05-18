import requests

url = "https://backend.blockadelabs.com/api/v1/skybox"

payload = "{\n    \"prompt\" : \"prompt example\",\n    \"negative_text\" : \"negative text example\",\n    \"skybox_style_id\" : 2\n}\n"
headers = {
  'x-api-key': '36GshOAMRxms4v8PwRkE1ykBzkaZQecWPOYEcHHGr5unOEibCUfGpBmKoJZM'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
