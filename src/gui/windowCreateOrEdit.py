from . import *

def open_new_page(newFile,selected_address):
    root.destroy()
    subprocess.run(["python", newFile, str(selected_address)])

# Fonction appelée lors du clic sur le bouton "Créer"
def create():
    open_new_page("/src/create.py",selected_address)

# Fonction appelée lors du clic sur le bouton "Modifier"
def modify():
    open_new_page(os.getcwd()+"/src/edit.py",selected_address)

def main():
    selected_address = sys.argv[1]

    # Création d'une interface simple
    root = tk.Tk()
    root.title("Créer ou Modifier")
    root.geometry("1024x740") 
    root.resizable(False, False) 
    root.iconphoto(True, ImageTk.PhotoImage(Image.open(os.getcwd()+"\\src\\images\\assets\\custom_icon.png")))

    background_image = Image.open(os.getcwd()+"\\src\\images\\assets\\background.jpg")  
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.style = ttk.Style()
    root.style.configure("Custom.TButton", foreground="black", background="#0078D4", font=("Helvetica", 28), padding=10)

    # Bouton pour créer
    create_button = ttk.Button(root, text="Créer",style="Custom.TButton", command=create)
    create_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Bouton pour modifier
    modify_button = ttk.Button(root, text="Modifier",style="Custom.TButton", command=modify)
    modify_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    root.mainloop()

if __name__ == "__main__":
    print("blalbalalnjoeznafi erzgui")