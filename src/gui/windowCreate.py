from PyOBEX.client import Client
from speechToText.speechToText import speak_and_transcribe
from speechToText import world_namer
from . import *
from imageGeneration import chooseStyleV3
from gui import windowValidation

# var globales
mic_waiting_image = None
mic_listening_image = None
mic_waiting_photo = None
mic_listening_photo = None
is_listening = False
button_image_id = None
device_address = None


def talk_to_text(canvas,root):
    global is_listening

    is_listening = True
    update_button_image(canvas)

    transcription = speak_and_transcribe()

    is_listening = False
    update_button_image(canvas)

    # Appeler la fonction pour envoyer l'image après la transcription
    text_to_image(transcription,root)

def text_to_image(prompt,root):
    status = chooseStyleV3.main(prompt)
    if status == "error":
        messagebox.showerror("An error occured", f"Could not generate image")
        root.destroy()
    else:
        send_image_to_device(status)
        windowValidation.main(root)

def update_button_image(canvas):
    if is_listening:
        canvas.itemconfig(button_image_id, image=mic_listening_photo)
    else:
        canvas.itemconfig(button_image_id, image=mic_waiting_photo)

def send_image_to_device(path):
    try:
        splitedPath = os.path.split(path)  
        fileName = splitedPath[1]  
        if device_address:
            service_matches = find_service(name=b'OBEX Object Push\x00', address=device_address)
            if len(service_matches) == 0:
                messagebox.showerror("Error", "Could not find the OBEX service.")
                return

            first_match = service_matches[0]
            port = first_match["port"]
            host = first_match["host"]
            client = Client(host, port)

            client.connect()
            with open(path, 'rb') as file:
                image_data = file.read()
            client.put(fileName, image_data)
            client.disconnect()

            messagebox.showinfo("Success", "Image sent successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main(root, selected_device_address):
    # Création de la fenêtre principale
    global mic_waiting_image, mic_listening_image, mic_waiting_photo, mic_listening_photo, button_image_id, device_address
    # On récupère l'adresse
    device_address = selected_device_address

    root.title("360VR")
      
    frame3 = tk.Frame(root)
    frame3.grid(row=0, column=0, sticky="nsew")

    background_image = ImageTk.PhotoImage(Image.open(DIRIMAGE + "background.jpg"))
    background_label = tk.Label(frame3, image=background_image)
    
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    # Talk frame pour parler
    talk_frame = tk.Frame(root, background="#0A75AD")
    talk_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Chargement des images de micro
    mic_waiting_image = Image.open(DIRIMAGE + "microphone_waiting.png")
    mic_waiting_image = mic_waiting_image.resize((200, 200))
    mic_waiting_photo = ImageTk.PhotoImage(mic_waiting_image)

    mic_listening_image = Image.open(DIRIMAGE + "microphone_listening.png")
    mic_listening_image = mic_listening_image.resize((200, 200))
    mic_listening_photo = ImageTk.PhotoImage(mic_listening_image)

    # represente le bouton pour parler
    canvas = tk.Canvas(talk_frame, width=250, height=250, bd=0, highlightthickness=0)
    canvas.create_oval(5, 5, 245, 245, fill="#0A75AD")
    canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button_image_id = canvas.create_image(125, 125, image=mic_waiting_photo)
    canvas.image = mic_waiting_photo

    # Listener pour le bouton
    canvas.bind("<Button-1>", lambda event: talk_to_text(canvas,root))
    canvas.pack()

    # Bouton pour parler
    # send_button = ttk.Button(talk_frame, text="Parler", command=talk_to_text, style="Custom.TButton")
    # send_button.pack()


    root.style = ttk.Style()
    root.style.configure("Custom.TButton", foreground="black", background="#0078D4", font=("Helvetica", 28), padding=10)

if __name__ == "__main__":
    print("Il n'y a aucun secret ici.. ou peut être..")