from Controllers.Database import Database as db

class Role:
    id = type(int)
    name = type(str)
    commands = []

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]

    def getPriviledges(self, role_id):
        """"get all priviledges from a role"""
        connect = db().connect()
        connect[1].execute('''SELECT * FROM Priviledges WHERE(SELECT * FROM rights WHERE roleid = ?), (id,)''')
        self.commands = connect[1].fetchall()
        db().saveandclose(connect)
