from . import *
from gui import windowValidation

def list_files(folder_path):
    # Vérifie si le chemin spécifié est un dossier
    if os.path.isdir(folder_path):
        # Liste tous les fichiers dans le dossier spécifié
        files = os.listdir(folder_path)
        return files
    else:
        return []

def send_image_to_device(root,files_listbox, device_address): 
    try:
        # Récuperation du chemin complet du fichier à envoyer
        file_index = files_listbox.curselection()
        file_name = files_listbox.get(file_index)
        file_path = os.path.join(DIRIMAGEGENERATED, file_name)  
        
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

            messagebox.showinfo("Success", "Image sent successfully.")
            windowValidation.main(root)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main(root,selected_device_address):
    root.title("Liste des fichiers")

    frame4 = tk.Frame(root)
    frame4.grid(row=0, column=0, sticky="nsew")
    background_image = ImageTk.PhotoImage(Image.open(DIRIMAGE + "background.jpg"))
    background_label = tk.Label(frame4, image=background_image) 
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image


    # Création de la liste 
    files_listbox = tk.Listbox(root)
    files_listbox.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    files_listbox.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    for file_name in list_files(DIRIMAGEGENERATED):
        files_listbox.insert(tk.END, file_name)
    
    # Bouton pour envoyer l'image
    send_button = ttk.Button(root, text="Send Image", style="Custom.TButton", command=lambda:send_image_to_device(root,files_listbox,selected_device_address))
    send_button.grid(row=1, column=0, padx=10, pady=5,sticky="nsew")
    send_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    root.style = ttk.Style()
    root.style.configure("Custom.TButton", foreground="black", background="#0078D4", font=("Helvetica", 28), padding=10)
    print(selected_device_address)

if __name__ == "__main__":
    print("QUITTE LA PAGE MAINTENANT !!!")
