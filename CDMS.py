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
        values = {}
        for x in instructions:
            values[x] = (input(f'{x} >>> '))
        return values

    def header(self, messages: list):
        self.clear()
        print('Welcome to the CDMS by Nathan Samijo 0961962\nPlease Login to continue')

    def login(self, usr):
        '''CHECK IF USER IS VALID'''
        users = Datahandler().getUsers()
        for user in users:
            if usr['username'] == user['username'] and usr['password'] == user['password']:
                return user
            if usr['username'] == self.super.username and usr['password'] == self.super.password:
                self.superadmin = True
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