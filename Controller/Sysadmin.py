from Controller.DataHandler import Datahandler
from Models.Person import Person


class Administrator:

    options = [
        'Clients',
        'Advisors',
        'Backup'
    ]
    option = None
    specialChars = "!@$%#&/:.?()=,*_[]~^-+`|\{};'<>"
    option = None

    def __init__(self, user: dict, person: dict):
        self.user = dict
        self.person = Person()
        self.person.setData(person)
        self.dh = Datahandler()

    def clear(self):
        print(50 * "\n")

    def choices(self):
        self.clear()
        print('Welcome to CDMS by Nathan Samijo 0961962')
        print(f'Naam: {self.person.getFullName()}\tPriviledge: System Administrator')
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

    def clients(self):
        clients = self.dh.getclients()

        while True:
            pointer = 1
            self.clear()
            print('Welcome to CDMS by Nathan Samijo 0961962')
            print(f'Naam: {self.person.getFullName()}\tPriviledge: System Administrator')
            print(f'Option: Clients\t [0] Back to menu\t[INSERT] Add new Client')

            print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(
                'Nr.',
                'Firstname',
                'Lastname',
                'Streetname',
                'Housenr',
                'Zipcode',
                'City',
                'Phone-nr',
                'Email')
            )
            for pers in clients:

                if pers['priviledge'] == 4:
                    print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(
                        f'[{pointer}]',
                        pers['firstName'],
                        pers['lastName'],
                        pers['streetName'],
                        pers['houseNumber'],
                        pers['zipCode'],
                        pers['city'],
                        pers['phoneNumber'],
                        pers['email'],
                        )
                    )
                    pointer += 1
            try:
                temp = input('Please select a Client >>> ')
                if temp != 'INSERT':
                    choice = int(temp)
            except:
                print('Please enter a valid option')

            while choice not in range(0, len(clients) + 1) and choice != 0 and choice != 'INSERT':
                try:
                    temp = input('Please select a Client >>> ')
                    if temp != 'INSERT':
                        choice = int(temp)
                except:
                    print('Please enter a valid option')
            if choice == 0:
                return
            elif choice == 'INSERT':
                continue
            else:
                self.client(clients[choice - 1])

    def client(self, person: dict):
        options = ['Firstname', 'Lastname', 'Streetname', 'Housenr', 'Zipcode', 'City', 'Email', 'Phone-nr']
        keys = ['firstName', 'lastName', 'streetName', 'houseNumber', 'zipCode', 'city', 'email', 'phoneNumber']
        clientoptions = ['1234567890', 'DELETE']
        EXIT = False

        while not EXIT:
            pointer = 0
            self.clear()
            print('CDMS by Nathan Samijo 0961962')
            print('[DELETE] Remove client\t[0] Back to client overview\t[9] Save changes')
            print('Enter a number from 1 to 8 to edit client information')
            print()
            for x in person.keys():
                # print(person)
                if not x in ['id', 'privilege']:
                    print(f'[{pointer + 1}] {options[pointer]} : {person[x]}')
                    pointer += 1

            choice = input('Client >>> ')
            while choice not in clientoptions or not len(choice) == 1:
                choice = input('Please enter a valid option >>> ')
            if choice in clientoptions[0]:
                choice = int(choice)
                if choice <= 8:
                    person[keys[choice - 1]] = input(f'Please enter a new value for {options[choice - 1]} >>>')
                elif choice == 9:
                    update = []
                    for x in keys:
                        update.append(person[x])
                    update.append(person['id'])
                    self.dh.updateperson(update)
                elif choice == 0:
                    EXIT = True
            elif choice == clientoptions[1]:
                self.dh.removePerson(person['id'])
                EXIT = True


    def optionhandler(self):
        if self.option == 1:
            self.clients()

    def menu(self):
        while self.option not in [0, 9]:
            self.choices()
            self.optionhandler()

        if self.option == 0:
            quit()
        if self.option == 9:
            return {}