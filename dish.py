class dish():
	def __init__(self,date=None,indications=None,name=None,price_s=None,price_e=None,price_g=None):
		""" price_s: pricing for students
			price_e: pricing for employees
			price_g: pricing for guests """
		self.date = date
		self.indications = indications
		if name == "":
			raise ValueError("name must not be empty or only whitespace!")
		self.name = name
		self.price_s = price_s
		self.price_e = price_e
		self.price_g = price_g

	# ljust indents the indications, so dishes with multiple (character
	# wide) flags do not fall out of line
	def __str__(self):
		s = "%s %s %s %s"%(self.date,str(self.indications).ljust(4),
			self.name,self.price_s)
		return s
