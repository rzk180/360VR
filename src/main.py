from gui import windowDeviceList
from utils import *
import tkinter as tk
from tkinter import messagebox, ttk


if __name__ == "__main__":
    windowDeviceList.main()
    print(windowDeviceList.get_selected_device_address())
