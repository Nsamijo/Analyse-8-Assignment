class Priviledge:
    id = type(int)
    name = type(str)

    def __init__(self, id, name):
        self.id = id
        self.name = name

        def database(self):
            """"function used to create database (resources.db)"""
            connect = self.connect()
            setcursor = connect.cursor()
            setcursor.execute(
                '''CREATE TABLE Clients ([id] INTEGER PRIMARY KEY, [fullname] VARCHAR[75], [adress] VARCHAR[50], [email] VARCHAR[50], [phone] VARCHAR[8])''')
            # rows admins
            setcursor.execute(
                '''CREATE TABLE Admins ([id] INTEGER PRIMARY KEY, [level] INTEGER, [username] VARCHAR[20], [password] VARCHAR[50])''')
            connect.commit()
            connect.close()

        def addsuperadmin(self):
            """"function used to add superadmin"""
            connect = self.connect()
            connect[1].execute('''INSERT INTO Admins(level, username, password) VALUES (1, "superadmin", "Admin!23")''')
            self.saveandclose(connect[0])

        def deleteuser(self, user, passwd):
            """"delete a admin/user from the system | can only be done by the superadmin and system admins"""
            connect = self.connect()
            query = 'DELETE FROM Admins WHERE username = ?'
            connect[1].execute(query, (user,))
            self.saveandclose(connect[0])

        def getalladmins(self):
            """"get all admins/users from the application"""
            connect = self.connect()
            connect[1].execute('''SELECT * FROM Admins''')
            return connect[1].fetchall()

    def execute(self, commands):
        option = []
        for key in commands.keys():
            option.append(key)


