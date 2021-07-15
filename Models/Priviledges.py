from Controllers.Database import Database
from Controllers.Encryption import Encryption

class Priviledge:
    id = type(int)
    name = type(str)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def database(self):
        """"function used to create database (resources.db)"""
        return
        connect = Database().connect()
        """command used to create priviledge table"""
        connect[0].execute('''CREATE TABLE priviledge(id INTEGER PRIMARY KEY AUTOINCREMENT, name CHAR(50))''')
        """command used to create rol table"""
        connect[0].execute('''CREATE TABLE role(id INTEGER PRIMARY KEY AUTOINCREMENT, name CHAR(15))''')
        """command used to create pivot table for roles and priviledges"""
        connect[0].execute('''CREATE TABLE rights(id INTEGER PRIMARY KEY AUTOINCREMENT, role_id INTEGER, priv_id INTEGER , FOREIGN KEY(role_id) REFERENCES role(id), FOREIGN KEY(priv_id) REFERENCES priviledge(id) )''')
        """command used to create the people table for client and admin data"""
        connect[0].execute('''CREATE TABLE people(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(25), surname VARCHAR(30), adres VARCHAR(75), email VARCHAR(100), username VARCHAR(20), pwd VARCHAR(30), registration_date VARCHAR(10), role_id INTEGER, FOREIGN KEY(role_id) REFERENCES role(id))''')
        Database().saveandclose(connect)

    def addRoles(self):
        """function used to add the roles in the database"""
        connect = Database().connect()
        #all available roles
        roles = ['client', 'advisor', 'sysadmin', 'super-admin']
        #encrypt the roles and then add them to the database
        for x in Encryption().encrypt(roles, 'role'):
            connect[0].execute('''INSERT INTO role(name) VALUES (?)''',(x,) )
        #save changes
        Database().saveandclose(connect)

    def deleteRoles(self):
        """function used to remove roles of needed"""
        #return added to disable functionality untill needed
        return
        connect = Database().connect()
        connect[1].execute('''SELECT * FROM role''')
        connect[1].execute('''DELETE FROM role WHERE id > 4''')
        print(connect[1].execute('''SELECT *  FROM role''').fetchall())
        Database().saveandclose(connect)

    def getRoles(self):
        """get all the roles form the database"""
        return Database().connect()[1].execute('''SELECT * FROM role''').fetchall()

    def updateRole(self):
        """update a role if needed"""
        connect = Database().connect()
        value = Encryption().encrypt('superadmin', 'role')
        connect[1].execute('''UPDATE role SET name = ? WHERE id = 3 ''', (value,))
        Database().saveandclose(connect)
