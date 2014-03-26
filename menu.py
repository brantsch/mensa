class menu():
	def __init__(self):
		self._dict = {}

	def append(self,date,dish):
		if not date in self._dict.keys():
			self._dict[date] = [dish]
		else:
			self._dict[date].append(dish)

	def __getitem__(self,key):
		return self._dict[key]

	def __contains__(self,key):
		return self._dict.__contains__(key)

	def __iter__(self):
		return self._dict.__iter__()

	def dates(self):
		return self._dict.keys()
