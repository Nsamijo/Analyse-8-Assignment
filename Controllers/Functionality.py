from Models.Priviledges import Priviledge

class Functions:

    priv = None
    def __init__(self):
        self.priv = Priviledge()

    def login(self, usr, pwd):
        for user in self.priv.loginfetch():
            if user[1] == usr and user[2] == pwd:
                return self.priv.accountdetails(user[0])
        return None