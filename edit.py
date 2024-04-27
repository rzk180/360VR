import tkinter as tk
from tkinter import messagebox
from bluetooth import *
from PyOBEX.client import Client
import subprocess

def list_files(folder_path):
    # Vérifie si le chemin spécifié est un dossier
    if os.path.isdir(folder_path):
        # Liste tous les fichiers dans le dossier spécifié
        files = os.listdir(folder_path)
        return files
    else:
        return []

def send_image_to_device(): 
    try:
        # Récuperation du chemin complet du fichier à envoyer
        file_index = files_listbox.curselection()
        file_name = files_listbox.get(file_index)
        file_path = os.path.join(folder_path, file_name)  
        
        # Si nous avons l'adresse bluetooth de l'appareil ciblé alors on initialise une connexion OBEX
        if device_address:
            service_matches = find_service(name=b'OBEX Object Push\x00', address=device_address)
            if len(service_matches) == 0:
                messagebox.showerror("Error", "Could not find the OBEX service.")
                return
            
            # Récupère les services et port disponibles
            first_match = service_matches[0]
            port = first_match["port"]
            host = first_match["host"]
            client = Client(host, port)
            
            # Connexion à l'appareil ciblé et envoi de l'image
            client.connect()
            with open(file_path, 'rb') as file:    
                image_data = file.read()
            client.put(file_name, image_data)
            client.disconnect()
            
            root.destroy()
            subprocess.run(["python", "validation.py"])
            messagebox.showinfo("Success", "Image sent successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    device_address = sys.argv[1]
    
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Liste des fichiers")

    # Chemin du dossier contenant les fichiers
    folder_path = '' # Mettre le chemin du dossier dans lequel seront stockés les images

    # Création de la liste 
    files_listbox = tk.Listbox(root)
    files_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    for file_name in list_files(folder_path):
        files_listbox.insert(tk.END, file_name)

    # Bouton pour envoyer l'image
    send_button = tk.Button(root, text="Send Image", command=send_image_to_device)
    send_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    # Affichage de la fenêtre
    root.mainloop()
