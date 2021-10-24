import sqlite3
from Controller.Encryption import Encryption


class Database:
####DATABASE CONNECTION HANDLER####

    def rows(self, person: bool):
        '''GET COLUMN NAMES FROM DATABASE'''
        columns = self.connect()
        if person:
            return [head[0] for head in  columns.execute('Select * from people').description]
        else:
            return [head[0] for head in columns.execute('Select * from users').description]

    def connect(self):
        ''''CONNECT TO DATABASE'''
        connect = sqlite3.connect('people.db')
        return connect

    def disconnect(self, connection):
        ''''END CONNECTION'''
        connection.commit()
        connection.close()

    def quicksql(self, sql):
        db = self.connect()
        data = db.execute(sql)
        data = data.fetchall()
        self.disconnect(db)
        return data

class Datahandler:

    def __init__(self):
        self.db = Database().connect()
        self.rows = Database().rows

    def getPeople(self):
        '''GET ALL PEOPLE IN THE SYSTEM'''
        people = []
        cols = self.rows(True)
        for person in Encryption().decrypt(Database().quicksql("SELECT * FROM people")):
            people.append(dict(zip(cols, person)))
        return people

    def getUsers(self):
        '''GET ALL USERS FROM THE SYSTEM'''
        users = []
        cols = self.rows(False)
        for user in Encryption().decrypt(Database().quicksql("SELECT * FROM users")):
            users.append(dict(zip(cols, user)))
        return users

    # def getlastid(self):

    def getPerson(self, value):
        '''GET A SINGULAR PERSON'''
        data = self.getPeople()
        people = []
        for x in data:
            if value in x.values():
                if isinstance(value, int):
                    return x
                people.append(x)
        return people

    def getUser(self, value):
        '''GET SINGULAR USER'''
        data = self.getUsers()
        people = []
        for x in data:
            if value in x.values():
                if isinstance(value, int):
                    return x
                people.append(x)
        if len(people) == 1:
            return people[0]
        return people

    def addPerson(self, person: list):
        '''ADD PERSON'''
        # print(person)
        Encryption().encrypt(person)
        self.db.execute("INSERT INTO people('priviledge', 'firstName', 'lastName', 'streetName', 'houseNumber', 'zipCode', 'city', 'email', 'phoneNumber') VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", person)
        self.db.commit()

    def removePerson(self, id):
        '''DELETE CLIENT / PERSON FROM DB'''
        self.db.execute("DELETE FROM people WHERE id = ?", (id,))
        self.db.commit()

    def removeuser(self, id: int):
        """REMOVE USER FROM LIST"""
        self.db.execute('DELETE FROM users WHERE pid = ?', (id,    ))
        self.db.commit()

    def addUser(self, user: list):
        '''ADD USER'''
        Encryption().encrypt(user)
        self.db.execute("INSERT INTO users VALUES(?, ?, ?)", user)
        self.db.commit()

    def updateperson(self, person):
        Encryption().encrypt(person)
        self.db.execute("update people set firstName = ?, lastName = ?, streetName = ?, houseNumber = ?, zipCode = ?, city = ?, email = ?, phoneNumber = ? where id = ?", person)
        self.db.commit()

    def updateuser(self, id, userdata: dict):
        '''UPDATE USERDATA'''
        edited = list(userdata.values())
        edited.append(id)
        Encryption().encrypt(edited)
        self.db.execute("update users set pid = ?, username = ?, password = ? where pid = ?", edited)
        self.db.commit()
