# Installer les modules pybluez, obex
# Commandes 'pip install pybluez'. Si échec de l'installation il faut utiliser 'pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez'. Module Obex 'pip install PyOBEX'
# Changer le chemin d'accès de l'image et l'adresse bluetooth de l'appareil. Si le chemin d'accès est le nom de l'image alors ne rien changer d'autre, sinon si c'est un chemin sous la forme /chemin/vers/le/ficher.jpg alors il faut remplacer image.path dans la fonction put() par le nom du fichier.

import tkinter as tk
from tkinter import messagebox
from bluetooth import *
from PyOBEX.client import Client
import subprocess

def open_new_page(selected_device_address):
    root.destroy()
    subprocess.run(["python", "createOrEdit.py", str(selected_device_address)])

# Scan les appareils bluetooth disponibles et les retournes dans une liste
def scan_devices():
    nearby_devices = discover_devices()
    device_list.delete(0, tk.END)  # Efface la liste actuelle
    for addr in nearby_devices:
        device_name = lookup_name(addr)
        device_list.insert(tk.END, device_name)

# Se connecte à l'appareil souhaité et retourne son adresse bluetooth
def connect_to_device():
    selected_device_index = device_list.curselection()
    if selected_device_index:
        selected_device_name = device_list.get(selected_device_index)
        selected_device_address = None
        nearby_devices = discover_devices()
        for addr in nearby_devices:
            if selected_device_name == lookup_name(addr):
                selected_device_address = addr
                messagebox.showinfo("Device Found", f"Found device: {selected_device_name} at address {addr}")        
                open_new_page(selected_device_address)
        if selected_device_address is None:
            messagebox.showerror("Device Not Found", f"Device {selected_device_name} not found")
    else:
        messagebox.showerror("Error", "Please select a device from the list.")

image_path = 'back.jpg'

# Création de la fenêtre principale
root = tk.Tk()
root.title("Bluetooth Image Sender")

# Liste des appareils Bluetooth
device_list = tk.Listbox(root)
device_list.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

# Scrollbar pour la liste des appareils
scrollbar = tk.Scrollbar(root, orient="vertical", command=device_list.yview)
scrollbar.grid(row=0, column=1, padx=0, pady=5, sticky="ns")
device_list.config(yscrollcommand=scrollbar.set)

# Bouton pour actualiser la liste des appareils
scan_button = tk.Button(root, text="Scan Devices", command=scan_devices)
scan_button.grid(row=1, column=0, padx=10, pady=5)

# Bouton pour se connecter à l'appareil sélectionné
connect_button = tk.Button(root, text="Connect", command=connect_to_device)
connect_button.grid(row=2, column=0, padx=10, pady=5)

root.mainloop()