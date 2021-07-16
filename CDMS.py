import time

from Controllers.Functionality import Functions
import os

from Models.Person import Client


class cdms:
    User = None
    Stop = False
    functions = None
    Screen = 1

    def __init__(self):
        self.functions = Functions()

    def clearscreen(self):
        os.system('cls')

    def login(self):
        """log in with credentials | check if the given username and password are of correct type"""
        username = input('Username >>> ')
        while len(username) < 5:
            username = input('Username [must have more than 5 characters]>>> ')

        pwd = input('Password >>> ')
        while len(pwd) < 8:
            pwd = input('Password [must have more than 8 characters]>>> ')
        data = self.functions.login(username, pwd)
        if data != None:
            self.User = Client(data)
        else:
            print('Username or Password is incorrect.')
            time.sleep(1.5)
            self.clearscreen()

    def startscreen(self):
        print('Welcome to the Clients Data Management System (CDSM)!\nPlease Login in to access the functionality:')

    def execute(self):
        if self.Screen == 1:
            self.startscreen()
            self.login()
            if self.User != None:
                self.Screen += 1