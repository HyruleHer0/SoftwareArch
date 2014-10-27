from Buyer import Buyer
from Item import Item

class Seller(Buyer):
    def __init__(self,name=None,address=None,age=None):
        Buyer.__init__(self,name,address,age)
        self._items = []
    def getitems(self):
        return self._items
    def additem(self, item):
        self._items.append(item)
