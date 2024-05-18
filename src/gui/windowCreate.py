from PyOBEX.client import Client
from . import *

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

def main(root,selected_device_address):
    # Création de la fenêtre principale    

    root.title("360VR")
      
    frame3 = tk.Frame(root)
    frame3.grid(row=0, column=0, sticky="nsew")

    background_image = ImageTk.PhotoImage(Image.open(DIRIMAGE + "background.jpg"))
    background_label = tk.Label(frame3, image=background_image)
    
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    # Bouton pour parler
    talk_frame = tk.Frame(root, bg="white")
    talk_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Bouton pour parler
    send_button = ttk.Button(talk_frame, text="Parler", command=talk_to_image, style="Custom.TButton")
    send_button.pack()


    root.style = ttk.Style()
    root.style.configure("Custom.TButton", foreground="black", background="#0078D4", font=("Helvetica", 28), padding=10)

if __name__ == "__main__":
    print("Il n'y a aucun secret ici.. ou peut être..")