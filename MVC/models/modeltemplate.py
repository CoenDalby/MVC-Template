import os
#filename = os.path.join(dirname, 'relative/path/to/file/you/want')

class Model:

    def __init__(self):
        self.stringsPath = os.path.dirname(__file__) + "/../../Data/strings.txt"
        
        return

    #The functions in the model
    #get or set data from an external
    #file and return it.
    def get_data(self):
        f = open(self.stringsPath, "r")
        data = f.read()
        f.close()
        return data

