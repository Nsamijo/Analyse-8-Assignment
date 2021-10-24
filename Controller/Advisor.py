import time
from Controller.DataHandler import Datahandler
from Models.Person import Person


class Advisor:
    options = [
        'Lookup Client',
        'Add Client',
        'Update Password'
    ]
    option = None
    specialChars = "!@$%#&/:.?()=,*_[]~^-+`|\{};'<>"

    def __init__(self, user: dict, person: dict):
        self.user = user
        self.person = Person()
        self.person.setData(person)
        self.dh = Datahandler()

    def clear(self):
        print(50 * "\n")

    def choices(self):
        '''PRINT ALL OPTIONS FOR ADVISOR'''
        self.clear()
        print('Welcome to CDMS by Nathan Samijo 0961962')
        print(f'Naam: {self.person.getFullName()}\tPriviledge: Advisor\n')
        print('[9] Logout \t[0] Exit CDMS\n')
        for x in range(0, len(self.options)):
            print(f'[{x + 1}] {self.options[x]}')
        self.option = input('Please choose an option >>> ')
        try:
            self.option = int(self.option)
        except:
            print('Please only enter numbers')

        while self.option not in [1, 2, 3, 9, 0]:
            try:
                self.option = int(input('Please choose a GIVEN option >>> '))
            except:
                print('Please only enter numbers')
        self.option = int(self.option)

    def optionshandler(self):
        '''HANDLE ALL THE OPTIONS'''
        if self.option == 1:
            self.lookupclient()
        elif self.options == 2:
            # self.addclient()
            print(self.dh.getPeople())
        elif self.option == 3:
            self.updatepassword()

    def lookupclient(self):
        '''LOOK UP A CLIENT'''
        user = ""
        while self.option != 8:
            self.clear()
            print('CDMS by Nathan Samijo 0961962')
            print(f'Option chosen: {self.options[self.option - 1]} \n[7] Update client \t[8] Back to menu\n')
            if user != "":
                urs = self.dh.getPerson(user)
                if isinstance(urs, list):
                    print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format('Firstname', 'Lastname','Streetname', 'Housenr','Zipcode', 'City', 'Phone-nr', 'Email'))
                    for pers in urs:
                        if pers['priviledge'] == 4:
                            print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(pers['firstName'], pers['lastName'], pers['streetName'], pers['houseNumber'], pers['zipCode'], pers['city'], pers['phoneNumber'], pers['email']))

            print()
            user = input('Client >>> ')
            if user.isdigit():
                if int(user) == 8:
                    self.option = 8
                elif int(user) == 7:
                    try:
                        self.alterclient(urs[0])
                    except:
                        print('Look up a client to update')

    def alterclient(self, person: dict, new=False):
        self.clear()
        options = ['Firstname', 'Lastname', 'Streetname', 'Housenr', 'Zipcode', 'City', 'Email', 'Phone-nr']
        keys = ['firstName', 'lastName', 'streetName', 'houseNumber', 'zipCode', 'city', 'email', 'phoneNumber']
        EXIT = False

        keysperson = list(person.keys())
        while not EXIT:
            pointer = 0
            self.clear()
            print('CDMS by Nathan Samijo 0961962')
            if not new:
                print(f'Option chosen: Update Client \n[9] Save Changes \t[0] Back to menu(Changes will not be saved)\n')
            else:
                print(
                    f'Option chosen: Add Client \n[9] Save Client \t[0] Back to menu(Changes will not be saved)\n')

            for x in keysperson:
                # print(person)
                if not x in ['id', 'privilege']:
                    print(f'[{pointer + 1}] {options[pointer]} : {person[x]}')
                    pointer += 1

            option = input('Please choose what to change >>> ')
            try:
                option = int(option)
            except:
                print('Please enter a valid option')
            while option not in range(0, 10):
                try:
                    option = int(input('Please choose what to change >>> '))
                except:
                    print('Please enter a valid option')
            if option == 9:

                if not new:
                    update = []
                    for x in keys:
                        update.append(person[x])
                    update.append(person['id'])
                    self.dh.updateperson(update)
                else:
                    person['privilege'] = 4
                    self.dh.addPerson(list(person.values()))
            elif option == 0:
                EXIT = True
            else:
                change = input(f'Please enter new value for {options[option - 1]} >>> ')
                person[keys[option - 1]] = change

    def updatepassword(self):

        def checkpw(password: str):
            if len(password) >= 8 and len(password) <= 30:
                has_nr = False
                has_sp = False
                has_cap = False
                has_low = False
                for x in password:
                    if x.isupper():
                        has_cap = True
                    if x.islower():
                        has_low = True
                    if x in self.specialChars:
                        has_sp = True
                    if x.isdigit():
                        has_nr = True
                return  has_cap and has_sp and has_low and has_nr
            if password == '0':
                return True
            return False

        self.clear()
        print('CDMS by Nathan Samijo 0961962')
        print(f'Option chosen: Update Password \n[0] Back to menu(Changes will not be saved)\n')
        print(f'Password requirements:\n- minimal length of 8\n- max length of 30\n- 1 capital letter\n- 1 lowercase letter\n- 1 number\n- 1 special character({self.specialChars})')
        pw = input('Please enter your new password >>> ')
        while not checkpw(pw):
            pw = input('New password does not meet all requirements: please enter a new password >>>')

        if pw == '0':
            return
        else:
            print(f'Password changed to: {pw}\nReturning to main menu')
            self.user['password'] = pw
            self.dh.updateuser(self.user['pid'], self.user)
            time.sleep(3)

    def addclient(self):
        keys = ['firstName', 'lastName', 'streetName', 'houseNumber', 'zipCode', 'city', 'email', 'phoneNumber']
        newclient = Person()
        #get last id and set new id for client

        for key in keys:
            if key not in ['id', 'priviledge']:
                newclient.__dict__[key] = ''
        self.alterclient(newclient.__dict__, new=True)




    def menu(self):
        '''ADVISOR MENU'''
        while self.option != 9 and self.option != 0:
            self.choices()
            self.optionshandler()

        if self.option == 0:
            quit()
        if self.option == 9:
            return {}
