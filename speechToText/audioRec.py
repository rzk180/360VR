import speech_recognition as sr

#Script d'écoute avec sélection du micro


def select_microphone():
    mic_list = sr.Microphone.list_microphone_names()
  
    print("Liste des microphones disponibles sur l'ordinateur :")
    for index, name in enumerate(mic_list):
        print(f"{index}: {name}")
    
    mic_number = int(input("Entrez le numéro du microphone à utiliser : "))
    if mic_number >= len(mic_list) or mic_number < 0:
        print("Numéro de microphone invalide. Veuillez réessayer.")
        return select_microphone()
    else:
        return mic_number

def speechToTextTranscriber(mic_number):
    r = sr.Recognizer()
    with sr.Microphone(device_index=mic_number) as source:
        r.adjust_for_ambient_noise(source)
        print("En écoute...")
        while True:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio, language="fr-FR")
                print("You said: " + text)
                if text.lower() == "confirmer": 
                    print("Stopping the listener.")
                    break
            except sr.UnknownValueError:
                print("L'audio n'a pas pu être compris.")
            except sr.RequestError as e:
                print(f"Erreur de requête; {e}")


mic_index = select_microphone()
speechToTextTranscriber(mic_index)
