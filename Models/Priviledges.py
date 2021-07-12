from Controllers.Database import Database

class Priviledge:
    id = type(int)
    name = type(str)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def database(self):
        """"function used to create database (resources.db)"""
        connect = Database().connect()
        """command used to create priviledge table"""
        #connect[0].execute('''CREATE TABLE priviledge(id INTEGER PRIMARY KEY AUTOINCREMENT, name CHAR(50))''')
        """command used to create rol table"""
        #connect[0].execute('''CREATE TABLE role(id INTEGER PRIMARY KEY AUTOINCREMENT, name CHAR(15))''')
        """command used to create pivot table for roles and priviledges"""
        #connect[0].execute('''CREATE TABLE rights(id INTEGER PRIMARY KEY AUTOINCREMENT, role_id INTEGER, priv_id INTEGER , FOREIGN KEY(role_id) REFERENCES role(id), FOREIGN KEY(priv_id) REFERENCES priviledge(id) )''')
        """command used to create the people table for client and admin data"""
        #connect[0].execute('''CREATE TABLE people(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(25), surname VARCHAR(30), adres VARCHAR(75), email VARCHAR(100), username VARCHAR(20), pwd VARCHAR(30), registration_date VARCHAR(10), role_id INTEGER, FOREIGN KEY(role_id) REFERENCES role(id))''')
        Database().saveandclose(connect)

    def execute(self, commands):
        option = []
        for key in commands.keys():
            option.append(key)
