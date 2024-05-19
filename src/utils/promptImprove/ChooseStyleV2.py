from openai import OpenAI
import random
import json
import re


client = OpenAI(
  api_key="sk-proj-OVwbFHSmAahojFbplHb1T3BlbkFJUI8ID5g5ztibeefMBUM0", 
)

def chat(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000  # Vous pouvez ajuster cette valeur selon la longueur de réponse souhaitée
    )
    return response.choices[0].text.strip()

def main(text):
    # Charger les données depuis le fichier JSON
    with open('Style3.json', 'r') as f:
        data = json.load(f)

    # Convertir le contenu en str
    resultat_str = json.dumps(data)

    # Exemple d'utilisation
    #Prompt argument apres pour un monde
    prompt = "Parmis ces styles "+ resultat_str +" choisi le style plus adapté pour un monde "+ text +", tu dois juste me renvoyer le numero de l'id sans aucun autre caractere."

    resultat_texte = chat(prompt)
    resultat_chiffres = re.findall(r'\d+', resultat_texte)  # Extraire les chiffres de la réponse
    resultat_entier = int(resultat_chiffres[0]) if resultat_chiffres else None  # Convertir le premier chiffre en entier, s'il existe

    list_id_M3 = [77, 121, 82, 112, 74, 81, 85, 87, 120, 75, 95, 122, 104, 90, 89, 67, 119, 115, 123, 80, 88, 118, 93, 114, 73, 68]

    if resultat_entier not in list_id_M3:
        resultat_entier = random.choice(list_id_M3)

    return resultat_entier
