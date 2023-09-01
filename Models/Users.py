from Database import Database
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
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
    
    def insert(self, username, email, password):
        conn = get_db_connection()
        # cursor = conn.cursor()
        conn.execute('INSERT INTO user (username, email, pass) VALUES (?, ?, ?)',
                       (username, email, password))
        
        conn.commit()
        conn.close()
    
