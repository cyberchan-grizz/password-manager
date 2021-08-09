import tkinter
from tkinter import *
import os
import passwordManager
from guiFunctions import *

root = Tk()
root.title("Key Keeper")
passwordManager = passwordManager()

os.path.expanduser("~")

try:
    open(os.path.expanduser("~") + "/ApplicationFiles/PasswordManager/PasswordFile.txt", "r")
    password_screen(root, passwordManager)
except FileNotFoundError:
    setup_screen(root, passwordManager)


root.mainloop()
passwordManager.update_password_file()
