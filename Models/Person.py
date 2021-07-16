from datetime import datetime
from Controllers.Encryption import Encryption

class Client:
    id = type(int)
    name = ""
    surname = ""
    adres = ""
    email = ""
    username = ""
    password = ""
    registrationdate = ""
    role_id = type(int)
    mobileNumber = ""

    def __init__(self):
        self.id = None

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.surname = data[2]
        self.adres = data[3]
        self.email = data[4]
        self.username = data[5]
        self.password = data[6]
        self.registrationdate= data[7]
        self.role_id = data[8]
        self.mobileNumber = data[9]

    def now(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    def fullName(self):
        ''''get the full name from client'''
        return self.name + self.surname

    def setNumber(self, nr):
        ''''set mobile number of client'''
        if len(nr) != 8 : return False
        self.mobileNumber = nr; return True

    def setName(self, name, first = True):
        ''''set first or surname of client'''
        if first: self.name = name; return
        self.surname = name

    def setEmail(self, email):
        ''''set email of client'''
        self.email = email

    def getsqlformat(self):
        return Encryption().encrypt([self.name, self.surname, self.adres, self.email, self.username, self.password, self.now(), self.role_id, self.mobileNumber], 'person')