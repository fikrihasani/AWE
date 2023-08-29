class Web:
    def __init__(self):
        pass

    def home(self):
        # this is text to render
        n = 12
        ls = []
        for i in range(n):
            ls.append("This is history of the essay used: "+i)
        return ls

    def result(self):
        # this will be used to handle result data to template of result
        focus = 7
        ideas = 7
        res = {
            "focus":focus,
            "ideas":ideas 
        }
        return res