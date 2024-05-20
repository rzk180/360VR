# src/utils/speechToText/speech_to_text.py

from openai import OpenAI
from . import world_namer
import speech_recognition as sr
import os

client = OpenAI()


#selection du micro
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


#ecoute du micro pour le speechToTest
def record_with_speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("En écoute...")
        audio = r.listen(source)
    return audio.get_wav_data()


#transcription avec openAI
def transcribe_with_openai(audio_data):
    temp_360vrprompt = 'temp_360vr_prompt.wav'
    with open(temp_360vrprompt, 'wb') as f:
        f.write(audio_data)
    
    with open(temp_360vrprompt, 'rb') as audio_file:
        translation = client.audio.translations.create(
            model="whisper-1",
            file=audio_file
        )

    os.remove(temp_360vrprompt)
    return translation.text


def speak_and_transcribe():
    audio_data = record_with_speech_recognition()
    return transcribe_with_openai(audio_data)


def save_prompt(transcription):
    try:
        #genere un nom de fichier par rapport au prompt donnée
        filename = world_namer.generate_filename(transcription)
        #écris la transcription audio dans le fichier
        with open("./user_prompts/" + filename, 'w') as f:
            f.write(transcription)
        print(f"Transcription audio: {filename}")
    except FileNotFoundError:
        print("File not found or transcription empty. Please try again.")


if __name__ == "__main__":
    speak_and_transcribe()
