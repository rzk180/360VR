import tkinter as tk
from tkinter import messagebox,ttk
from bluetooth import *
from PyOBEX.client import Client
from PIL import Image, ImageTk
import subprocess
import os

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
    root.geometry("1024x740") 
    root.resizable(False, False) 
    root.iconphoto(True, ImageTk.PhotoImage(Image.open(os.getcwd()+"\\images\\assets\\custom_icon.png")))


    background_image = Image.open(os.getcwd()+"\\images\\assets\\background.jpg") 
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Chemin du dossier contenant les fichiers
    folder_path = os.getcwd()+'\\images' # Mettre le chemin du dossier dans lequel seront stockés les images

    # Création de la liste 
    files_listbox = tk.Listbox(root)
    files_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    files_listbox.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    for file_name in list_files(folder_path):
        files_listbox.insert(tk.END, file_name)
    
    # Bouton pour envoyer l'image
    send_button = ttk.Button(root, text="Send Image", style="Custom.TButton", command=send_image_to_device)
    send_button.grid(row=1, column=0, padx=10, pady=5,sticky="nsew")
    send_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    root.style = ttk.Style()
    root.style.configure("Custom.TButton", foreground="black", background="#0078D4", font=("Helvetica", 28), padding=10)

    root.mainloop()
