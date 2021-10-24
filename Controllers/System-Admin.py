from Advisor import Advisor

class SystemAdmin:

    options = [
        'Clients',
        'Advisors',
        'Backup'
    ]
    option = None
    specialChars = "!@$%#&/:.?()=,*_[]~^-+`|\{};'<>"

    def __init__(self, user: dict):
        self.user = dict

    def menu(self):
        print('CDMS by Nathan Samijo 0961962')