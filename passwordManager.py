import cryptography
from passwordProfile import *
from applicationSettings import *
from cryptography.fernet import Fernet
import os
import pickle
import hashlib


homeDir = os.path.expanduser("~")

class passwordManager(object):

    def setup(self, password):
        #try loading the password file, if the file doesnt exist then set the masterpassword to nothing
        try:
            passwordFile = open(homeDir + "/ApplicationFiles/PasswordManager/PasswordFile.txt", "rb")
            self.masterPass = pickle.load(passwordFile)

            # if Master Password equals the password entered by the user then try to open read the passwordProfile file
            if (self.masterPass == str(hashlib.md5(password.encode()).hexdigest())):
                print("Correct Password Entered")
                try:
                    passwordProfileFile = open(homeDir + "/ApplicationFiles/PasswordManager/PasswordProfileFile.txt", "rb")
                    self.profileList = pickle.load(passwordProfileFile)

                    with open(homeDir + "/ApplicationFiles/PasswordManager/PassProfileEncryptionFile.key") as key:
                        self.encryptionKey = Fernet(key.read())
                    for profile in self.profileList:
                        profile.change_title(self.encryptionKey.decrypt(profile.get_title()).decode())
                        profile.change_username(self.encryptionKey.decrypt(profile.get_username()).decode())
                        profile.change_password(self.encryptionKey.decrypt(profile.get_password()).decode())


                    print("Profile List Loaded From File")
                    return "Profile List Loaded From File"
                except EOFError:
                    print("New Profile List Created")
                    self.profileList = []
                    return "New Profile List Created"
            else:
                print("Incorrect Password Entered")
                return "Incorrect Password Entered"

        except FileNotFoundError:
            setup()
            passwordFile = open(homeDir + "/ApplicationFiles/PasswordManager/PasswordFile.txt", "wb")

            with open(homeDir + "/ApplicationFiles/PasswordManager/PassProfileEncryptionFile.key", "rb") as keyFile:
                self.key = keyFile.read()

            #password encryption and save
            encodedPassword = password.encode()
            hashedPassword = hashlib.md5(encodedPassword)
            hashedPassword = str(hashedPassword.hexdigest())
            pickle.dump(hashedPassword, passwordFile)

            self.masterPass = hashedPassword
            self.profileList = []

            print("Setup Completed")

    def get_profile_list(self):
        return self.profileList

    def add_password_profile(self, passwordProfile):
        self.profileList.append(passwordProfile)

    def get_profile(self, profileName):
        for profile in self.profileList:
            if(profile.get_title() == profileName):
                return profile

    def delete_profile(self, profileName):
        for profile in self.profileList:
            if(profile.get_title() == profileName):
                self.profileList.remove(profile)
                return

    def change_username(self, profileName, newUsername):
        for profile in self.profileList:
            if(profile.get_title() == profileName):
                profile.change_username(newUsername)
                return

    def change_password(self, profileName, newPassword):
        for profile in self.profileList:
            if(profile.get_title() == profileName):
                profile.change_password(newPassword)
                return

    def change_title(self, oldProfileName, newProfileName):
        for profile in self.profileList:
            if(profile.get_title() == oldProfileName):
                profile.change_title(newProfileName)
                return

    def update_password_file(self):
        passwordProfileFile = open(homeDir + "/ApplicationFiles/PasswordManager/PasswordProfileFile.txt", "wb")

        with open(homeDir + "/ApplicationFiles/PasswordManager/PassProfileEncryptionFile.key") as key:
            self.encryptionKey = Fernet(key.read())
        for profile in self.profileList:
            profile.change_title(self.encryptionKey.encrypt(profile.get_title().encode()))
            profile.change_username(self.encryptionKey.encrypt(profile.get_username().encode()))
            profile.change_password(self.encryptionKey.encrypt(profile.get_password().encode()))

        pickle.dump(self.profileList, passwordProfileFile)
