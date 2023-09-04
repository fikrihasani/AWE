from Database import Database
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

class Article:
    def __init__(self):
        self.conn = Database().conn
        self.data = None

    def getAll(self):
        data = []
        for i in range(12):
            data.append("this is article the "+str(i))
        return data
    
    def getOne(self,id):
        return []
    
    def getAll2(self):
        self.data = []
        data = self.conn.execute("SELECT * FROM essay").fetchall()
        self.conn.close()
        return data

    def insert(self, essayInput, userID):
        conn = get_db_connection()
        # cursor = conn.cursor()
        conn.execute('INSERT INTO essay (content, userID) VALUES (?, ?)',
                       (essayInput, userID))
        
        conn.commit()
        conn.close()

    
