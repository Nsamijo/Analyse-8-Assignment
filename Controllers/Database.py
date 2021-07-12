import sqlite3


class Database:

    def connect(self):
        """"connect to database"""
        conn = sqlite3.connect('resources.db')
        return [conn, conn.cursor()]

    def nuke(self, connection):
        connection[0].close()

    def saveandclose(self, connection):
        connection[0].commit()
        self.nuke(connection)