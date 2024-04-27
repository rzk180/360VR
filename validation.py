import subprocess
import tkinter as tk
import sys

 
text= "Veuillez regarder l'image sur l'appareil séléctionné"
create_window = tk.Tk()
 
# specify size of window.
create_window.geometry("250x170")
 
# Create text widget and specify size.
T = tk.Text(create_window, height = 5, width = 52)
 
# Create label
l = tk.Label(create_window, text = "Fact of the Day")
l.config(font =("Courier", 14))
 
 
# Create an Exit button.
b2 = tk.Button(create_window, text = "Exit",
            command = create_window.destroy) 
 
l.pack()
T.pack()
b2.pack()
 
# Insert The Fact.
T.insert(tk.END, text)
 
tk.mainloop()
