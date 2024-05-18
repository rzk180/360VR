from . import *
from gui import windowCreate,windowEdit

# Fonction appelée lors du clic sur le bouton "Créer"
def create(root,selected_device_address):
    windowCreate.main(root,selected_device_address)

# Fonction appelée lors du clic sur le bouton "Modifier"
def modify(root,selected_device_address):
    windowEdit.main(root,selected_device_address)

def raise_frame(frame):
    frame.tkraise()

def main(root,selected_device_address):
    # Création d'une interface simple

    frame2 = tk.Frame(root)
    frame2.grid(row=0, column=0, sticky="nsew")

    background_image = ImageTk.PhotoImage(Image.open(DIRIMAGE + "background.jpg"))
    background_label = tk.Label(frame2, image=background_image)
    
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    raise_frame(frame2)

    root.style = ttk.Style()
    root.style.configure("Custom.TButton", foreground="black", background="#0078D4", font=("Helvetica", 28), padding=10)

    # Bouton pour créer
    create_button = ttk.Button(frame2, text="Créer",style="Custom.TButton", command=lambda:create(root,selected_device_address))
    create_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Bouton pour modifier
    modify_button = ttk.Button(frame2, text="Modifier",style="Custom.TButton", command=lambda:modify(root,selected_device_address))
    modify_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    print(selected_device_address)

if __name__ == "__main__":
    print("blalbalalnjoeznafi erzgui")