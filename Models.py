class Article:
    def __init__(self):
        pass

    def getAll(self):
        # this is text to render
        # ambil data dari database
        n = 12
        ls = ["This is history of the essay used: "+str(i) for i in range(n)] 
        return ls

    def getAllFrom(self, userId):
        pass

    def getOne(self,id):
        pass
