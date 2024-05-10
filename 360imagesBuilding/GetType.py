import requests
import json

url = "https://backend.blockadelabs.com/api/v1/skybox/export"

payload = {}
headers = {
  'x-api-key': '36GshOAMRxms4v8PwRkE1ykBzkaZQecWPOYEcHHGr5unOEibCUfGpBmKoJZM'
}

response = requests.request("GET", url, headers=headers, data=payload)
datas = response.json()

# Ouvrir un fichier en mode écriture
with open("TypeExport.json", "w") as fichier:
    # Écrire les données JSON dans le fichier
    json.dump(datas, fichier, indent=4)

print("Les données ont été écrites dans le fichier TypeExport.json")