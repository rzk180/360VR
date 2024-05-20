import requests
import random
import json


def chat_gpt(prompt):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "{API_KEY}"
    }
    data = {
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 2000
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        print("Erreur lors de la requête :", response.text)
        return None

# style model 3 STR
with open('Style3.json', 'r') as f:
    data = json.load(f)

# Convertir le contenu en str
resultat_str = json.dumps(data)

# Exemple d'utilisation
#Prompt argument apres pour un monde
prompt = "parmis ces styles "+ resultat_str +" choisi le style plus adapté pour un monde "+ "au dessus des nuages avec juste le ciel bleu comme au paradis" +", tu dois juste me renvoyer le numero de l'id sans aucun autre caractere."

result=(chat_gpt(prompt))


list_id_M3 = [77, 121, 82, 112, 74, 81, 85, 87, 120, 75, 95, 122, 104, 90, 89, 67, 119, 115, 123, 80, 88, 118, 93, 114, 73, 68]

if result not in list_id_M3:
    result = random.choice(list_id_M3)


print(result)