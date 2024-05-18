from . import *

selected_device_address = None

# Scan les appareils bluetooth disponibles et les retournes dans une liste
def scan_devices(device_list):
    nearby_devices = discover_devices()
    device_list.delete(0, tk.END)  # Efface la liste actuelle
    for addr in nearby_devices:
        device_name = lookup_name(addr)
        device_list.insert(tk.END, device_name)

# Se connecte à l'appareil souhaité et retourne son adresse bluetooth
def connect_to_device(device_list):
    global selected_device_address
    selected_device_index = device_list.curselection()
    if selected_device_index:
        selected_device_name = device_list.get(selected_device_index)
        selected_device_address = None
        nearby_devices = discover_devices()
        for addr in nearby_devices:
            if selected_device_name == lookup_name(addr):
                selected_device_address = addr
                messagebox.showinfo("Device Found", f"Found device: {selected_device_name} at address {addr}")        
                return selected_device_address
        if selected_device_address is None:
            messagebox.showerror("Device Not Found", f"Device {selected_device_name} not found")
    else:
        messagebox.showerror("Error", "Please select a device from the list.")

def get_selected_device_address():
    return selected_device_address

def main():
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Bluetooth Image Sender")
    root.geometry("1024x740") 
    root.resizable(False, False) 
    root.iconphoto(True, ImageTk.PhotoImage(Image.open(DIRIMAGE + "custom_icon.png")))  

    # Charger et afficher une image en arrière-plan
    background_image = ImageTk.PhotoImage(Image.open(DIRIMAGE + "background.jpg"))
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Liste des appareils Bluetooth
    device_list = tk.Listbox(root)
    device_list.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

    # Scrollbar pour la liste des appareils
    scrollbar = tk.Scrollbar(root, orient="vertical", command=device_list.yview)
    scrollbar.grid(row=0, column=1, padx=0, pady=5, sticky="ns")
    device_list.config(yscrollcommand=scrollbar.set)

    # Bouton pour actualiser la liste des appareils avec le style Windows 11
    scan_button = ttk.Button(root, text="Scan Devices", command=lambda:scan_devices(device_list), style="W.TButton")
    scan_button.grid(row=1, column=0, padx=10, pady=5)

    # Définition du style Windows 11 pour le bouton Scan Devices
    root.style = ttk.Style()
    root.style.configure("W.TButton", foreground="black", background="#0078D4", font=("Helvetica", 12, "bold"), padding=10)

    # Bouton pour se connecter à l'appareil sélectionné avec le style Windows 11
    connect_button = ttk.Button(root, text="Connect", command=lambda:connect_to_device(device_list), style="W.TButton")
    connect_button.grid(row=2, column=0, padx=10, pady=5)

    # Boucle principale pour l'affichage de la fenêtre
    root.mainloop()

if __name__ == "__main__":
    print("Veuillez executer le fichier main.py")