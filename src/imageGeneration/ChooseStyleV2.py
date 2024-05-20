from openai import OpenAI
import requests
import os
import random
import json
import re




def chat(prompt):
    api_key = "{API_KEY}"
    url = "https://api.openai.com/v1/completions"

    params = {
        "model": "gpt-3.5-turbo",  # Modèle GPT à utiliser
        "prompt": prompt,             # Votre prompt
        "max_tokens": 100             # Nombre maximal de tokens dans la réponse
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(url, json=params, headers=headers)

    return response

def main(text):
    # Charger les données depuis le fichier JSON
    with open(os.getcwd() + '\src\imageGeneration\data\Style3.json', 'r') as f:
        data = json.load(f)

    # Convertir le contenu en str
    resultat_str = json.dumps(data)

    list_id_M3 = [77, 121, 82, 112, 74, 81, 85, 87, 120, 75, 95, 122, 104, 90, 89, 67, 119, 115, 123, 80, 88, 118, 93, 114, 73, 68]
    chaine_id_M3 = ''.join(map(str, list_id_M3)) 

    # Exemple d'utilisation
    #Prompt argument apres pour un monde
    prompt = "dis moi bonjour"

    print( chat(prompt))
    """
    print(resultat_texte)
    resultat_chiffres = re.findall(r'\d+', resultat_texte)  # Extraire les chiffres de la réponse
    print(resultat_chiffres)
    resultat_entier = int(resultat_chiffres[0]) if resultat_chiffres else None  # Convertir le premier chiffre en entier, s'il existe

    if resultat_entier not in list_id_M3:
        resultat_entier = random.choice(list_id_M3)
    
    print(resultat_entier)
    """
if __name__ == "__main__":
    main("un chateau et trois arbres")