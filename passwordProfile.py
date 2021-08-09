from passwordGenerator import *

class passwordProfile(object):
    def __init__(self, Title, Password, Username=None):
        self.Title = Title
        self.Username = Username
        self.Password = Password

    def change_password(self, newPassword):
        self.Password = newPassword

    def get_password(self):
        return self.Password

    def change_username(self, newUsername):
        self.Username = newUsername

    def get_username(self):
        return self.Username

    def change_title(self, newTitle):
        self.Title = newTitle

    def get_title(self):
        return self.Title

