import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

def send_image_to_device():
    try:
        # Votre code pour envoyer l'image à l'appareil sélectionné
        pass
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("360VR")
    root.geometry("1024x740")
    root.resizable(False, False)
    root.iconphoto(True, ImageTk.PhotoImage(Image.open(os.getcwd()+"\\src\\images\\assets\\custom_icon.png")))
    
    # Charger et afficher une image en arrière-plan
    background_image = Image.open(os.getcwd()+"\\src\\images\\assets\\background.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
 
    # Création du widget de texte et spécification de la taille
    T = tk.Text(root, height=5, width=52)
 
    # Création du label et centrage horizontal et vertical
    l = tk.Label(root, text="Fact of the Day")
    l.config(font=("Helvetica", 14))
    l.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
 
    # Placement du cadre légèrement plus bas
    T.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
 
    # Création du bouton pour fermer la fenêtre avec le style Windows 11 et centrage horizontal
    b2 = ttk.Button(root, text="Exit", command=root.destroy, style="W.TButton")
    b2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    
    # Définition du style Windows 11 pour le bouton
    root.style = ttk.Style()
    root.style.configure("W.TButton", foreground="black", background="#0078D4", font=("Helvetica", 12, "bold"), padding=10)

    # Insertion du texte dans le widget de texte
    T.insert(tk.END, "Veuillez regarder l'image sur l'appareil sélectionné")
 
    # Boucle principale pour l'affichage de la fenêtre
    root.mainloop()