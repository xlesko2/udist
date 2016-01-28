from product import ProductType, Product
from vector2d import Vector2D
from collections import deque

class Organization(object):
	'''
	Class representing a 'place' in the world, such as a factory or store.
	Virtual class, inherited only by Factory so far.
	'''
	name = 'Organization'
	
	def __init__(self, position):
		assert isinstance(position, Vector2D), 'position not a Vector2D.'
		self.position = position
		return None

class Factory(Organization):
	'''
	Class representing a single manufacturing unit.
	The factory is placed on a certain position in the game world,
	and manufactures a product based on its specification.
	'''
	name = 'Factory'

	def __init__(self, product_type, capacity, position):
		'''
		Params:
			-- product_type - produced ProductType ref
			-- capacity - int, production per time unit
			-- position - 2D Vector that positions factory in game world
		'''
		Organization.__init__(self, position)
		
		assert isinstance(product_type, ProductType),\
			'product_type not a ProductType'
		self.product_type = product_type
		
		assert isinstance(capacity, int), 'capacity not an int.'
		self.capacity = int(capacity/self.product_type.difficulty)
		
		# storage of required materials
		self.storage = dict()
		for item in self.product_type.requirements:
			self.storage[item] = 0
		
		# output queue
		self.output = deque()
		
		return None
	
	def __repr__(self):
		return '<Factory, ID={0}, position={1}, capacity={2}, product={3}>'.format(
			hex(id(self)), self.position, self.capacity, self.product_type.name)
	
	def __str__(self):
		return 'Factory at {0} producing {1}.\n'.format(
			self.position, self.product_type.name)\
			+ 'Storage state:\n{0}\n'.format('\n'.join(['-- {0}: {1} units'.format(
					key.name, self.storage[key]) for key in self.storage]))\
					+ 'Output queue length: {0}'.format(len(self.output))
	
	def material_sufficient(self):
		return int(min([self.storage[i]/self.product_type.requirements[i]\
			for i in self.storage]))
	
	def produce(self):
		amount = min([self.material_sufficient(), self.capacity])
		for item in self.product_type.requirements:
			self.storage[item] -= amount * self.product_type.requirements[item]
		for p in range(amount):
			self.output.append(Product(self.product_type))
		return None

ziemiaciek = ProductType('Ziemiaciek', {}, 1.00)
a = Factory(ziemiaciek, 220, Vector2D(10,10))
b = Factory(ProductType('Pluszowy Mort', {ziemiaciek: 100}, 1.02), 470, Vector2D(12,10))
