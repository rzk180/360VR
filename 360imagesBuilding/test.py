import json

with open('Style3.json', 'r') as f:
    data = json.load(f)

# Convertir le contenu en str
resultat_str = json.dumps(data)

nombre_de_caracteres = len(resultat_str)

print("Nombre de caractères dans Style3.json:", nombre_de_caracteres)