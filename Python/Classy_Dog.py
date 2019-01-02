class Dog():
	"""A simple attempt to model a dog."""
	
	def _init_(self,name,age):
		"""Initialize name and age attributes."""
		self.name=name
		self.age=age
		
	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling ocver in response to a command."""
		print(self.name.title() + " rolled over!")
		
