from Models.Privilege import Privilege


class Person:
    id = ""
    firstName = ""
    lastName = ""
    streetName = ""
    houseNumber = ""
    zipCode = ""
    city = ""
    email = ""
    phoneNumber = ""
    privilege = None

    def __init__(self):
        ''''SET PRIVILEDGE ON INIT'''
        self.privilege = Privilege.CLIENT

    def getFullName(self):
        ''''GET FULL NAME OF PERSON'''
        return f'{self.firstName} {self.lastName}'

    def getAddress(self):
        ''''GET FULL ADDRESS OF PERSON'''
        # Goed gebruik van f-strings
        return f'{self.streetName} {self.houseNumber} {self.zipCode} {self.city}'

    def getPriviledge(self): # Houd je naming van Privilege consistent, privileDge is verkeerd gespeld.
        ''''GET PRIVILEDGE LEVEL OF PERSON'''

        # Houd je code DRY (Don't Repeat Yourself)
        if self.privilege is None:
            pass # Doe iets om de None case af te handelen, mss [Privilege.CLIENT.name, Privilege.CLIENT.value]
        else:
            return [self.privilege.name, self.privilege.value]


        # if self.privilege == Privilege.SUPER_ADMINISTRATOR:
        #     return ['SUPER ADMIN', 1]
        # elif self.privilege == Privilege.SYSTEM_ADMINISTRATOR:
        #     return ['SYSTEM ADMIN', 2]
        # elif self.privilege == Privilege.ADVISOR:
        #     return ['ADVISOR', 3]
        # return ['CLIENT', 4]

    def getPerson(self): # Zou dit getData noemen, meer inline met je setData functie.
        return self.__dict__

    def setData(self, persondict):
        self.__dict__ = persondict



class Advisor(Person):
    """Docstrings zoe je met triple quotes"""
####ADVISOR: HANDLES CLIENTS####
    pid = None
    username = ""
    password = ""
    def __init__(self):
        # Gebruik super() ipv person
        # https://stackoverflow.com/a/576183
        super().__init__()
        # Person.__init__(self)
        self.privilege = Privilege.ADVISOR

    # Deze twee functies doen hetzelfde als Person.getPerson en Person.setData
    def dictUser(self):
        return self.__dict__

    def setUser(self, user):
        self.__dict__ = user


class SystemAdmin(Advisor):
####SYSTEM ADMININISTRATOR: HANDLES ADVISORS AND CLIENTS####

    def __init__(self):
        Advisor.__init__(self)
        self.privilege = Privilege.SYSTEM_ADMINISTRATOR


class SuperAdmin(Advisor):
####HARDCODED SUPERADMIN AS STATED IN ASSIGNMENT: HANDLES SYSTEM ADMINISTRATORS, ADVISORS AND CLIENTS####

    def __init__(self):
        Advisor.__init__(self)
        self.privilege = Privilege.SUPER_ADMINISTRATOR
        self.username = 'superadmin'
        self.password = 'Admin!23'
