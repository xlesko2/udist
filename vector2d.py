import math

class Vector2D(object):
	'''
	Class representing a 2D vector. Implemented for convenience
	of being able to call x and y parametres of coordinates explicitly.
	'''
	name = 'Vector2D'
	
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
	
	def __eq__(self, other):
		assert isinstance(other, Vector2D), 'other not a Vector2D'
		return self.x == other.x and self.y == other.y
	
	def __lt__(self, other):
		assert isinstance(other, Vector2D), 'other not a Vector2D'
		return (self.x, self.y) < (other.x, other.y)
	
	def __le__(self, other):
		assert isinstance(other, Vector2D), 'other not a Vector2D'
		return (self.x, self.y) <= (other.x, other.y)
			
	def __len__(self):
		return math.sqrt(self.x**2 + self.y**2)
	
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
	
	def __repr__(self):
		return '<Vector2D, ID={0}, x={1}, y={2})'.format(hex(id(self)),
			self.x, self.y)
	
	def __str__(self):
		return 'v({0},{1})'.format(self.x, self.y)
	
	def __hash__(self):
		return hash((self.x, self.y))

u = Vector2D(10,10)
v = Vector2D(8,69)
