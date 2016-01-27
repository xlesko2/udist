class Vector2D(object):
	'''
	Class representing a 2D vector. Implemented for convenience
	of being able to call x and y parametres of coordinates explicitly.
	'''
	def __init__(self, x = 0, y = 0):
		def is_number(x):
			try:
				float(x)
				return True
			except ValueError:
				return False
		
		assert is_number(x), 'Non-numerical x value: {0}'.format(x)
		assert is_number(y), 'Non-numerical y value: {0}'.format(y)
		self.x = x
		self.y = y
		return None
	
	def __str__(self):
		return '({0}, {1})'.format(self.x, self.y)
	
	def __add__(self, other):
		assert type(other) is type(self), "{0} is not a vector".format(other)
		return Vector2D(self.x + other.x, self.y + other.y)
	
	def __sub__(self, other):
		assert type(other) is type(self), "{0} is not a vector".format(other)
		return self + other*(-1)
	
	def __mul__(self, scalar):
		return Vector2D(*map(lambda i: i*scalar, [self.x, self.y]))
	
	def __rmul__(self, scalar):
		return self.__mul__(scalar)
	
	def __truediv__(self, scalar):
		assert scalar != 0, 'Tried to divide vector by zero.'
		return self * (1/scalar)
	
	def __floordiv__(self, scalar):
		assert scalar != 0, 'Tried to divide vector by zero.'
		return Vector2D(*map(lambda i: int(i/scalar), [self.x, self.y]))

a = Vector2D(42,69)
b = a/2
