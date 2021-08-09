import os
import pickle
import cryptography
from cryptography.fernet import Fernet

def clear_widgets(widgetList):
    for widget in widgetList:
        widget.destroy()


def setup():
    print("Running Setup...")
    homeDir = os.path.expanduser("~")

    os.system("mkdir " + homeDir + "/ApplicationFiles")
    os.system("mkdir " + homeDir + "/ApplicationFiles/PasswordManager")
    os.system("touch " + homeDir + "/ApplicationFiles/PasswordManager/PasswordFile.txt")
    os.system("touch " + homeDir + "/ApplicationFiles/PasswordManager/PasswordProfileFile.txt")
    os.system("touch " + homeDir + "/ApplicationFiles/PasswordManager/PassProfileEncryptionFile.key")

    profileKey = Fernet.generate_key()
    with open(homeDir + "/ApplicationFiles/PasswordManager/PassProfileEncryptionFile.key", "wb") as keyFile:
        keyFile.write(profileKey)

