class Buyer:
	def __init__(self):
		self._name = None
		self._address = None
		self._age = None
	
	def name(self):
		return self._name
	
	def name(self, value):
		self._name = value
	
	def address(self):
		return self._address
		
	def address(self, value):
		self._address = value
		
	def age(self):
		return self._age
	
	def age(self, value):
		self._age = value
