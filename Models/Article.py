from Database import Database

class Article:
    def __init__(self):
        pass

    def getAll(self):
        data = []
        for i in range(12):
            data.append("this is article the "+str(i))
        return data
    
    def getOne(self,id):
        return []
    
