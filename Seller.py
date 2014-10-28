from Buyer import Buyer
from Item import Item

class Seller:
    def __init__(self,name=None,address=None,age=None):
        self._name = name
        self._address = address
        self._age = age
        
    #Set information functions    
    def age(self, age):
        self._age = age
        
    def getname(self):
        return self._name
    
    def getaddress(self):
        return self._address
    #Return information functions  
    def getage(self):
        return self._age
        
    def name(self, name):
        self._name = name
        
    def address(self, address):
        self._address = address
    
    
        
    

