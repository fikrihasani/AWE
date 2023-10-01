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

    def getOne(self, essayId):
        self.data = []
        data = self.conn.execute("SELECT * FROM essay where id = ?", (essayId,)).fetchone()
        self.conn.close()
        return data
    
    def getAll(self,id):
        self.data = []
        data = self.conn.execute("SELECT * FROM essay WHERE userId = ?", (id,)).fetchall()
        self.conn.close()
        return data 
    
    def getAll2(self):
        self.data = []
        data = self.conn.execute("SELECT * FROM essay").fetchall()
        self.conn.close()
        return data

    def insert(self, essayInput, userID, score1, score2):
        conn = get_db_connection()
        # cursor = conn.cursor()
        print("SCORES = " , score1  , score2)
        str_score1 = str(score1)
        str_score2 = str(score2)
        conn.execute('INSERT INTO essay (content, userID, scoreFocusnPurpose, ideasnDevelopment) VALUES (?, ?, ?, ?)',
                       (essayInput, userID, str_score1, str_score2))
        
        lastId = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        print(lastId)
        
        conn.commit()
        conn.close()

        return lastId

    def updateEssay(self, id, newEssay, newScore1, newScore2):
        conn = get_db_connection()
        
        str_score1 = str(newScore1)
        str_score2 = str(newScore2)
        conn.execute('UPDATE essay SET content = ?, scoreFocusnPurpose = ?, ideasnDevelopment = ? WHERE id = ?',
                        (newEssay, str_score1, str_score2, id))
        
        conn.commit()
        conn.close()

