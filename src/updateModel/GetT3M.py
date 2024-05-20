import requests
import json

url = "https://backend.blockadelabs.com/api/v1/skybox/styles"

payload = {}

headers = {
  'x-api-key': '{API_KEY}'
}

response = requests.request("GET", url, headers=headers, data=payload)
#LIST
datas = response.json()
# Créer un dictionnaire vide pour stocker les données converties
#STR
datas_str = json.dumps(datas)
#DICT
datas_dict = json.loads(datas_str)

print(type(datas_dict))
print(datas_dict['id'])
# Assumer que chaque élément de la liste a une propriété 'id' comme clé unique
#for item in datas:
    # Utiliser la valeur de 'id' comme clé dans le dictionnaire
    # et l'ensemble de l'élément comme valeur associée
#    datas_dict[item['id']] = item

# Maintenant, datas_dict est un dictionnaire où les clés sont les 'id'
# et les valeurs sont les éléments complets de la liste

# Tu peux maintenant accéder aux données comme avant mais en utilisant datas_dict
#nom_description = datas_dict['id']['name']['description']

# Ouvrir un fichier en mode écriture
with open("Style3.json", "w") as f:
    # Écrire les données JSON dans le fichier
    json.dump(datas_dict, f, indent=4)

print("Les données ont été écrites dans le fichier Style3.json")