class Client:
    id = type(int)
    name = ""
    surname = ""
    adress = ""
    email = ""
    mobileNumber = ""
    username = ""
    password = ""
    registrationdate = ""
    role_id = type(int)


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