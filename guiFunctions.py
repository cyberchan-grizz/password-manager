import tkinter
from tkinter import *
from applicationSettings import *
from passwordManager import *


def setup_screen(root, passwordManager, currentWidgets = []):

    def checkForMatch(pass1, pass2):
        if (pass1 == pass2):
            # open password manager
            passwordManager.setup(pass1)
            password_manager_screen(root, passwordManager, widgets)
            return
        else:
            # have user input passwords again
            incorrectPassPrompt = Label(root, text = "Passowrds Don't Match", width = 40, anchor = "center")
            incorrectPassPrompt.grid(row=3)
            widgets.append(incorrectPassPrompt)
            submitButton.grid(row=4)
            exitButton.grid(row=5)

    def clear_entry(entryBox):
        if (entryBox.get() == "Enter New Password" or entryBox.get() == "Confirm New Password"):
            entryBox.delete(0, END)
            entryBox.configure(show="•")

    clear_widgets(currentWidgets)
    widgets = []

    welcomeLabel = Label(root, text = "Welcome to Key Keeper!", anchor = "center")
    welcomeLabel.grid(row=0)
    widgets.append(welcomeLabel)

    passwordEntry = Entry(root, width=40)
    passwordEntry.insert(0, "Enter New Password")
    passwordEntry.bind('<Button-1>', lambda event:[clear_entry(entryBox=passwordEntry)])
    passwordEntry.bind('<FocusIn>', lambda event:[clear_entry(entryBox=passwordEntry)])
    passwordEntry.grid(row=1)
    widgets.append(passwordEntry)

    confirmPasswordEntry = Entry(root, width=40)
    confirmPasswordEntry.insert(0, "Confirm New Password")
    confirmPasswordEntry.bind('<Button-1>', lambda event:[clear_entry(entryBox=confirmPasswordEntry)])
    confirmPasswordEntry.bind('<FocusIn>', lambda event:[clear_entry(entryBox=confirmPasswordEntry)])
    confirmPasswordEntry.grid(row=2)
    widgets.append(confirmPasswordEntry)

    submitButton = Button(root, text="Submit", width=37,
                          command=lambda: [checkForMatch(passwordEntry.get(), confirmPasswordEntry.get())])
    submitButton.grid(row=3)
    widgets.append(submitButton)

    exitButton = Button(root, text = "Exit", width = 37, command = lambda:[root.destroy()])
    exitButton.grid(row=4)
    widgets.append(exitButton)

def password_screen(root, passwordManager, currentWidgets = []):

    def submit_button(password):
        #open password manager
        result = passwordManager.setup(password)
        if(result == "Incorrect Password Entered"):
            incorrectPassPrompt = Label(root, text = "Incorrect Password Entered", width = 40, anchor = "center")
            incorrectPassPrompt.grid(row=2)
            widgets.append(incorrectPassPrompt)
            submitButton.grid(row=3)
            exitButton.grid(row=4)
        else:
            password_manager_screen(root, passwordManager, widgets)


    def clear_entry(entryBox):
        if (entryBox.get() == "Enter Password"):
            entryBox.delete(0, END)
            entryBox.configure(show="•")

    clear_widgets(currentWidgets)
    widgets = []

    welcomeLabel = Label(root, text="Welcome to Key Keeper!", anchor="center")
    welcomeLabel.grid(row=0)
    widgets.append(welcomeLabel)

    passwordEntry = Entry(root, width=40)
    passwordEntry.insert(0, "Enter Password")
    passwordEntry.bind('<Button-1>', lambda event: [clear_entry(entryBox=passwordEntry)])
    passwordEntry.bind('<FocusIn>', lambda event: [clear_entry(entryBox=passwordEntry)])
    passwordEntry.grid(row=1)
    widgets.append(passwordEntry)

    submitButton = Button(root, text="Submit", width=37, command=lambda:[submit_button(passwordEntry.get())])
    submitButton.grid(row=2)
    widgets.append(submitButton)

    exitButton = Button(root, text = "Exit", width = 37, command = lambda:[root.destroy()])
    exitButton.grid(row=3)
    widgets.append(exitButton)

def password_manager_screen(root, passManager, currentWidgets = [], search=False):

    def search_func():
        if(searchBar.get() == "" or searchBar.get() == "Enter Profile Title"):
            password_manager_screen(root, passManager, widgets, False)
        else:
            password_manager_screen(root, passManager, widgets, True)

    def clear_entry(entryBox):
        entryBox.delete(0, END)

    def reveal_password(passwordElement, passwordProfile, button):
        if(passwordElement.cget("text") != "PASSWORD: ••••••••••••••••••••"):
            passwordElement.configure(text="PASSWORD: ••••••••••••••••••••")
            button.configure(text="Reveal")
        else:
            passwordElement.configure(text="PASSWORD: " + passwordProfile.get_password())
            button.configure(text="Hide")


    def edit_profile(passwordElement):
        edit_profile_screen(root, passwordElement, passManager, widgets)

    clear_widgets(currentWidgets)
    widgets = []

    title = Label(root, text = "Key Keeper", width = 40, anchor = "center")
    title.grid(row=0, columnspan=3)
    widgets.append(title)

    addProfileButton = Button(root, text="+", width = 2, command = lambda:[add_profile_screen(root, passManager, widgets)])
    addProfileButton.grid(row=1, sticky="w")
    widgets.append(addProfileButton)

    searchBar = Entry(root, width = 20)
    searchBar.grid(row=1, column=1, sticky="w")
    searchBar.insert(0, "Enter Profile Title")
    searchBar.bind("<Button-1>", lambda event: clear_entry(searchBar))
    widgets.append(searchBar)

    searchButton = Button(root, text = "Search", width = 10, command = lambda:[search_func()])
    searchButton.grid(row=1, column=2, sticky="w")
    widgets.append(searchButton)


    if(len(passManager.profileList) == 0):
        promptLabel = Label(root, text = 'click "+" to add new profile', width = 40, anchor = "center")
        promptLabel.grid(row=2, columnspan=3)
        widgets.append(promptLabel)

        logoutButton = Button(root, text="Logout", width=37, command=lambda: [password_screen(root, passManager, widgets)])
        logoutButton.grid(row=3, columnspan=3)
        widgets.append(logoutButton)
    else:
        row = 4

        if(search == False):
            for passProf in passManager.profileList:
                title = Label(root, text = "TITLE: " + passProf.get_title(), width = 40, anchor="w")
                title.grid(row=row, column=0, sticky="w", columnspan=3)
                widgets.append(title)

                row += 1

                username = Label(root, text = "USERNAME: " + passProf.get_username(), width = 30, anchor = "w")
                username.grid(row=row, column=0, sticky="w", columnspan=2)
                widgets.append(username)

                editButton = Button(root, text="Edit", width=10, command=lambda passwordProfile=passProf:[edit_profile(passwordProfile)])
                editButton.grid(row=row, column=2, sticky="w")
                widgets.append(editButton)

                row += 1

                dotPass = "••••••••••••••••••••"
                password = Label(root, text = "PASSWORD: " + dotPass, width = 30, anchor = "w")
                password.grid(row=row, column=0, sticky="w", columnspan=2)
                widgets.append(password)

                revealButton = Button(root, text = "Reveal", width = 10)
                revealButton.configure(command = lambda passwordElement=password, passwordProfile=passProf, button=revealButton:[reveal_password(passwordElement, passwordProfile, button)])
                revealButton.grid(row=row, column=2, sticky="w")
                widgets.append(revealButton)

                row += 1
        else:
            for passProf in passManager.profileList:
                if(searchBar.get() in passProf.get_title()):
                    title = Label(root, text="TITLE: " + passProf.get_title(), width=40, anchor="w")
                    title.grid(row=row, column=0, sticky="w", columnspan=3)
                    widgets.append(title)

                    row += 1

                    username = Label(root, text="USERNAME: " + passProf.get_username(), width=30, anchor="w")
                    username.grid(row=row, column=0, sticky="w", columnspan=2)
                    widgets.append(username)

                    editButton = Button(root, text="Edit", width=10,
                                        command=lambda passwordProfile=passProf: [edit_profile(passwordProfile)])
                    editButton.grid(row=row, column=2, sticky="w")
                    widgets.append(editButton)

                    row += 1

                    dotPass = "••••••••••••••••••••"
                    password = Label(root, text="PASSWORD: " + dotPass, width=30, anchor="w")
                    password.grid(row=row, column=0, sticky="w", columnspan=2)
                    widgets.append(password)

                    revealButton = Button(root, text="Reveal", width=10)
                    revealButton.configure(
                        command=lambda passwordElement=password, passwordProfile=passProf, button=revealButton: [
                            reveal_password(passwordElement, passwordProfile, button)])
                    revealButton.grid(row=row, column=2, sticky="w")
                    widgets.append(revealButton)

                    row += 1
            if(row == 4):
                notFoundPrompt = Label(root, text = "ERROR : Password Profile Not Found", anchor = "center")
                notFoundPrompt.grid(row=row, column=0, columnspan=3)
                widgets.append(notFoundPrompt)
        row += 1
        logoutButton = Button(root, text="Logout", width=37, command=lambda:[password_screen(root, passManager, widgets)])
        logoutButton.grid(row=row, columnspan=3)
        widgets.append(logoutButton)


def add_profile_screen(root, passwordManager, currentWidgets = []):

    def add_profile(title, username, password):
        if(title == ""  or password == ""):
            errorPrompt = Label(root, text = "ERROR : Please Fill Out All Required Feilds", width = 40, anchor = "center")
            errorPrompt.grid(row=4, columnspan=3)
            widgets.append(errorPrompt)

            addProfileButton.grid(row=5, columnspan=3)
            backButton.grid(row=6, columnspan=3)

        else:
            prof = passwordProfile(title, password, Username=username)
            passwordManager.add_password_profile(prof)


    clear_widgets(currentWidgets)
    widgets = []

    titleLabel = Label(root, text = "Key Keeper", width = 40, anchor = "center")
    titleLabel.grid(row=0, columnspan=3)
    widgets.append(titleLabel)

    namePrompt = Label(root, text = "Name: ", width = 10, anchor = "center")
    namePrompt.grid(row=1, column=0)
    widgets.append(namePrompt)

    nameEntry = Entry(root, width = 30)
    nameEntry.grid(row=1, column=1, columnspan=2, sticky="w")
    widgets.append(nameEntry)

    usernamePrompt = Label(root, text = "Username:", width = 10, anchor = "center")
    usernamePrompt.grid(row=2, column=0)
    widgets.append(usernamePrompt)

    usernameEntry = Entry(root, width = 30)
    usernameEntry.grid(row=2, column=1, columnspan=2, sticky="w")
    widgets.append(usernameEntry)

    passwordPrompt = Label(root, text = "Password:", width = 10, anchor = "center")
    passwordPrompt.grid(row=3, column=0)
    widgets.append(passwordPrompt)

    passwordEntry = Entry(root, width = 20)
    passwordEntry.configure(show="•")
    passwordEntry.grid(row=3, column=1, sticky="w")
    widgets.append(passwordEntry)

    genPasswordButton = Button(root, text = "Generate", width = 6, command = lambda:[passwordEntry.delete(0, END), passwordEntry.insert(0, generate_password(17))])
    genPasswordButton.grid(row=3, column=2, sticky="w")
    widgets.append(genPasswordButton)

    addProfileButton = Button(root, text = "Add Profile", width = 37, command = lambda:[add_profile(nameEntry.get(), usernameEntry.get(), passwordEntry.get()), password_manager_screen(root, passwordManager, widgets)])
    addProfileButton.grid(row=4, columnspan=3)
    widgets.append(addProfileButton)

    backButton = Button(root, text = "Back", width = 37, command = lambda:[password_manager_screen(root, passwordManager, widgets)])
    backButton.grid(row=5, columnspan=3)
    widgets.append(backButton)


def edit_profile_screen(root, passwordProfile, passwordManager, currentWidgets=[]):

    def update_profile(newTitle, newUsername, newPassword):
        passwordManager.change_title(passwordProfile.get_title(), newTitle)
        passwordManager.change_username(passwordProfile.get_title(), newUsername)
        passwordManager.change_password(passwordProfile.get_title(), newPassword)

    clear_widgets(currentWidgets)
    widgets = []

    titleLabel = Label(root, text="Key Keeper", width=40, anchor="center")
    titleLabel.grid(row=0, columnspan=3)
    widgets.append(titleLabel)

    namePrompt = Label(root, text="Name: ", width=10, anchor="center")
    namePrompt.grid(row=1, column=0)
    widgets.append(namePrompt)

    nameEntry = Entry(root, width=30)
    nameEntry.grid(row=1, column=1, columnspan=2, sticky="w")
    nameEntry.insert(0, passwordProfile.get_title())
    widgets.append(nameEntry)

    usernamePrompt = Label(root, text="Username:", width=10, anchor="center")
    usernamePrompt.grid(row=2, column=0)
    widgets.append(usernamePrompt)

    usernameEntry = Entry(root, width=30)
    usernameEntry.grid(row=2, column=1, columnspan=2, sticky="w")
    usernameEntry.insert(0, passwordProfile.get_username())
    widgets.append(usernameEntry)

    passwordPrompt = Label(root, text="Password:", width=10, anchor="center")
    passwordPrompt.grid(row=3, column=0)
    widgets.append(passwordPrompt)

    passwordEntry = Entry(root, width=20)
    passwordEntry.configure(show="•")
    passwordEntry.grid(row=3, column=1, sticky="w")
    passwordEntry.insert(0, passwordProfile.get_password())
    widgets.append(passwordEntry)

    genPasswordButton = Button(root, text="generate", width=6, command=lambda: [passwordEntry.delete(0, END), passwordEntry.insert(0, generate_password(17))])
    genPasswordButton.grid(row=3, column=2, sticky="w")
    widgets.append(genPasswordButton)

    updateProfileButton = Button(root, text="Update Profile", width=37, command=lambda: [update_profile(nameEntry.get(), usernameEntry.get(), passwordEntry.get()), password_manager_screen(root, passwordManager, widgets)])
    updateProfileButton.grid(row=4, columnspan=3)
    widgets.append(updateProfileButton)

    deleteProfileButton = Button(root, text ="Delete Profile", width=37, command=lambda: [passwordManager.delete_profile(passwordProfile.get_title()), password_manager_screen(root, passwordManager, widgets)])
    deleteProfileButton.grid(row=5, columnspan=3)
    widgets.append(deleteProfileButton)

    backButton = Button(root, text="Back", width=37, command=lambda: [password_manager_screen(root, passwordManager, widgets)])
    backButton.grid(row=6, columnspan=3)
    widgets.append(backButton)






