class Screen(object):
	"""docstring for Student"""
	@property
	def width(self):
		return self._width
	@width.setter

	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('input an integer')
		self._width=value

	@width.deleter
	def width(self):
		del self._width

	@property
	def heigth(self):
		return self._heigth

	@heigth.setter
	def heigth(self,value):
		if not isinstance(value,int):
			raise ValueError('input an integer')
		self._heigth=value 

	@heigth.deleter
	def heigth():
		del self._heigth

	@property
	def resolution(self):
		self._resolution=self._width*self._heigth
		return self._resolution
s=Screen()
s.width=13
s.heigth=13
print(s.width,s.heigth,s.resolution)