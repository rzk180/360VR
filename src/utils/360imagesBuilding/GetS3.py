import json

# Charger le fichier JSON
with open('donnees.json', 'r') as f:
    data = json.load(f)

# Filtrer les éléments avec la clé "model_version" ayant pour valeur "3"
result = [{"id": element["id"], "name": element["name"], "description": element["description"]} 
          for element in data if element.get('model_version') == "3"]

with open('Style3.json', 'w') as f2:
    json.dump(result, f2, indent=4)

print("Les données ont été écrites dans le fichier Style3.json")
