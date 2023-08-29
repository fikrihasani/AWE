from Database import Database

class Users:
    def __init__(self):
        self.conn = Database().conn
        self.data = None

    def getAll(self):
        self.data = []
        data = self.conn.execute("SELECT * FROM user").fetchall()
        self.conn.close()
        return data

    def getOne(self,id):
        self.data = []
        data = self.conn.execute("SELECT * FROM user where id = "+str(id)).fetchone()
        self.conn.close()
        return data
    
