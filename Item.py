class Item:
    def __init__(self,name,start,desc=None):
        self._name = name
        self._start = start
        self._desc = desc

    def getname (self):
        return self._name

    def name (self,name):
        self._name = name

    def getstart (self):
        return self._start

    def start (self,start):
        self._start = start

    def getdesc (self):
        return self._desc

    def desc (self, desc):
        self._desc = desc
        
