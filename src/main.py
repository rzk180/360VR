from gui import windowDeviceList
from utils import *
import tkinter as tk
from PIL import ImageTk, Image
import os


if __name__ == "__main__":
    
    root = tk.Tk()
    root.geometry("1024x740") 
    root.resizable(False, False) 
    root.iconphoto(True, ImageTk.PhotoImage(Image.open(os.getcwd()+"\\src\\assets\\guiAssets\\custom_icon.png")))

    # Configuration de la grille pour que la frame principale s'étende
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    windowDeviceList.main(root)

    root.mainloop()