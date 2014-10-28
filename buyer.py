class Buyer:
	def __init__(self,name=None,address=None,age=None):
		self._name = name
		self._address = address
		self._age = age
	
	def getname(self):
		return self._name
	
	def name(self, value):
		self._name = value
	
	def getaddress(self):
		return self._address
		
	def address(self, value):
		self._address = value
		
	def getage(self):
		return self._age
	
	def age(self, value):
		self._age = value

