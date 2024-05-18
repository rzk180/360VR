import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from bluetooth import *
from PIL import ImageTk, Image
import subprocess
from PyOBEX.client import Client

DIR=os.getcwd() + "\\src\\gui\\"
DIRIMAGE= os.getcwd() + "\\src\\assets\\guiAssets\\"
DIRIMAGEGENERATED = os.getcwd() + "\\src\\assets\\generated\\"