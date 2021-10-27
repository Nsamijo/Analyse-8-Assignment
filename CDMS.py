from Controller.Advisor import Advisor
from Controller.Sysadmin import Administrator
from Models.Person import *
from Models.Privilege import *
from Controller.DataHandler import Datahandler

class CDMS:
    user = {}
    exit = "EXIT"
    choice = None

    def __init__(self):
        self.dh = Datahandler()
        self.super = SuperAdmin()
        self.superadmin = False

    def clear(self):
        print(50 * "\n")

    def getinput(self, instructions):
        # Het is duidelijk wat deze functie doet als je het leest,
        # maar een comment met uitleg is toch handig.
        values = {}
        for x in instructions:
            values[x] = (input(f'{x} >>> '))
        return values

    def header(self, messages: list):
        self.clear()
        print('Welcome to the CDMS by Nathan Samijo 0961962\nPlease Login to continue')

    def login(self, usr):
        # Je zou de parameter usr kunnen hernoemen naar credentials of cred, dat is logischer.
        # Op dit moment is het namelijk nog geen user, het zijn login gegevens.
        '''CHECK IF USER IS VALID'''
        users = Datahandler().getUsers()
        for user in users:
            if usr['username'] == user['username'] and usr['password'] == user['password']:
                return user
            # Als je ooit een geval tegen komt waarbij je if (condition) then return True/False
            # krijgt, dan kan je het vervangen door gewoon de condition te returnen:
            self.superadmin = usr['username'] == self.super.username and usr['password'] == self.super.password
            # In veel gevallen maakt dit je code leesbaarder sneller, omdat branchen dmv een if-statement traag is.

            # if usr['username'] == self.super.username and usr['password'] == self.super.password:
            #     self.superadmin = True
        return {}

    def execute(self):
        while self.choice != self.exit:
            self.header(['Please login to continue'])
            while self.user == {} and not self.superadmin:
                self.user = self.login(self.getinput(["username", "password"]))

            if self.superadmin:
                print('Logged in as Super Admin')
                quit()
            else:
                person = self.dh.getPerson(self.user['pid'])
                #initialize users based on priviledge level
                if Privilege(person['priviledge']) == Privilege.ADVISOR:
                    self.user = Advisor(self.user, person)
                elif Privilege(person['priviledge']) == Privilege.SYSTEM_ADMINISTRATOR:
                    self.user = Administrator(self.user, person)
                    self.user.clients()
                # self.user = self.user.menu()