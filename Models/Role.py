from Controllers.Database import Database as db

class Role:
    id = type(int)
    name = type(str)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getPriviledges(self):
        """"get all priviledges from a role"""
        connect = db().connect()
        connect[1].execute('''SELECT * FROM Priviledges WHERE(SELECT * FROM Pivot WHERE roleid = ?), (id,)''')
        results = connect[1].fetchall()
        db().saveandclose(connect)
        return results
