import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, ttk
from bluetooth import *
from PyOBEX.client import Client
import subprocess
import os

def talk_to_image():
    # code pour parler et générer les images mettre la fonction send_image_to_device à la fin de la fonction pour un envoi automatique
    print("print a effacer c'est juste pour pas avoir une fonction vide")

def send_image_to_device():
    try:
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
            with open(selected_file_name, 'rb') as file: #remplacer la variable selected_file_name par le chemin vers l'image généré
                image_data = file.read()
            client.put(selected_file_name, image_data) #remplacer la variable selected_file_name par le chemin vers l'image généré
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
    root.title("360VR")
    root.geometry("1024x740") 
    root.resizable(False, False) 
    root.iconphoto(True, ImageTk.PhotoImage(Image.open(os.getcwd()+"\\src\\images\\assets\\custom_icon.png")))
    

    background_image = Image.open(os.getcwd()+"\\src\\images\\assets\\background.jpg")  
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Bouton pour parler
    talk_frame = tk.Frame(root, bg="white")
    talk_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Bouton pour valider et générer l'image
    send_button = ttk.Button(talk_frame, text="Parler", command=talk_to_image, style="Custom.TButton")
    send_button.pack()


    root.style = ttk.Style()
    root.style.configure("Custom.TButton", foreground="black", background="#0078D4", font=("Helvetica", 28), padding=10)


    root.mainloop()
