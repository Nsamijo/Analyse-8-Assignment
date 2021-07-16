from Controllers.Database import Database
from Controllers.Encryption import Encryption
from datetime import datetime

class Priviledge:
    id = type(int)
    name = type(str)

    def now(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def database(self):
        """"function used to create database (resources.db)"""
        #disable function until needed
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
        #disabled the function till needed again
        return
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

    def updateRole(self):
        """update a role if needed"""
        #disabled untill needed again
        return
        connect = Database().connect()
        value = Encryption().encrypt('superadmin', 'role')
        connect[1].execute('''UPDATE role SET name = ? WHERE id = 3 ''', (value,))
        Database().saveandclose(connect)

    def addClient(self, name, surname, adres, email,username=None, password=None, access="client"):
        """Function used to create add a new person to the database | access level must be defined"""
        #role id which correntsponts with the roles
        e = Encryption().encrypt
        type = 'person'
        roleid = {'client': 1, 'advisor': 2, 'sysadmin': 3, 'superadmin': 4}[access]
        connection = Database().connect()
        connection[1].execute('''INSERT INTO people (name, surname, adres, email, username, pwd, registration_date, role_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (e(name, type), e(surname, type), e(adres, type), e(email, type), e(username, type), e(password, type), str(e(self.now(), type)), e(roleid, type),))
        Database().saveandclose(connection)

    def add(self, cmd="", ins=""):
        lock = Encryption()
        connection = Database().connect()
        cmdl = lock.encrypt(cmd, 'priviledge')
        insl = lock.encrypt(ins, 'priviledge')
        #connection[1].execute('''DELETE FROM rights WHERE id = 6''')
        connection[1].execute('''ALTER TABLE people ADD COLUMN mobilenr''')
        #connection[1].execute("INSERT INTO priviledge (name, instruction) VALUES (?, ?)", (cmdl, insl,))
        Database().saveandclose(connection)

    def fetch(self, command, key='person', grouped=False):
        """function used to fetch entire tables"""
        if grouped:
            rawdata = Database().connect()[1].execute(command).fetchall()
            bundleddata = []
            for row in rawdata:
                bundleddata.append(Encryption().decrypt(row, key))
            return bundleddata
        return Encryption().decrypt(Database().connect()[1].execute(command).fetchall(), key)

    def loginfetch(self):
        return self.fetch('SELECT id, username, pwd FROM people', grouped=True)

    def accountdetails(self, pk):
        return Encryption().decrypt(Database().connect()[1].execute("SELECT * FROM people WHERE id = ?", (pk,)).fetchone(), 'person')
