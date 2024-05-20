from . import *

def main(root):

    root.title("360VR")

    
    # Charger et afficher une image en arrière-plan
    frame5 = tk.Frame(root)
    frame5.grid(row=0, column=0, sticky="nsew")
    background_image = ImageTk.PhotoImage(Image.open(DIRIMAGE + "background.jpg"))
    background_label = tk.Label(frame5, image=background_image) 
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image
 
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
 

if __name__ == "__main__":
    print("VOUS VENEZ DE GAGNER UN IPHONE 15 PRO !! Renseignez vos coordonnées bancaires pour réclamer votre gain. ")