import subprocess
import tkinter as tk
import sys

def open_new_page(newFile,selected_address):
    root.destroy()
    subprocess.run(["python", newFile, str(selected_address)])

# Fonction appelée lors du clic sur le bouton "Créer"
def create():
    open_new_page("create.py",selected_address)

# Fonction appelée lors du clic sur le bouton "Modifier"
def modify():
    open_new_page("edit.py",selected_address)

if __name__ == "__main__":
    
    # Récuperation de l'adresse bluetooth
    selected_address = sys.argv[1]
    
    # Création d'une interface simple
    root = tk.Tk()
    root.title("Créer ou Modifier")
    
    # Bouton pour créer
    create_button = tk.Button(root, text="Créer", command=create)
    create_button.pack(pady=10)

    # Bouton pour modifier
    modify_button = tk.Button(root, text="Modifier", command=modify)
    modify_button.pack(pady=10)

    root.mainloop()