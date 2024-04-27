import subprocess
import tkinter as tk
import sys

def open_new_page(newFile,selected_address):
    create_modify_window.destroy()
    subprocess.run(["python", newFile, str(selected_address)])

# Fonction appelée lors du clic sur le bouton "Créer"
def create():
    open_new_page("create.py",selected_address)
    print("Créer")

# Fonction appelée lors du clic sur le bouton "Modifier"
def modify():
    open_new_page("edit.py",selected_address)
    print("Modifier")

if __name__ == "__main__":
    selected_address = sys.argv[1]
    create_modify_window = tk.Tk()
    create_modify_window.title("Créer ou Modifier")
    
    # Bouton pour créer
    create_button = tk.Button(create_modify_window, text="Créer", command=create)
    create_button.pack(pady=10)

    # Bouton pour modifier
    modify_button = tk.Button(create_modify_window, text="Modifier", command=modify)
    modify_button.pack(pady=10)

    print(selected_address) 
    create_modify_window.mainloop()