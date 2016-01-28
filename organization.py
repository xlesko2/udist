from product import ProductType
from vector2d import Vector2D

class Organization(object):
	'''
	Class representing a 'place' in the world, such as a factory or store.
	Virtual class inherited by Factory.
	'''
	name = 'Organization'
	pass

class Factory(Organization):
	'''
	Class representing a single manufacturing unit.
	The factory is placed on a certain position in the game world,
	and manufactures a product based on its specification.
	'''
	name = 'Factory'
	
	def __init__(self, product_type, speed, position):
		'''
		Params:
			-- product_type - produced ProductType ref
			-- speed - float, coefficient of product manufacture type
			-- position - 2D Vector that positions factory in game world
		'''
		assert isinstance(product_type, ProductType),\
			'product_type not a ProductType'
		self.product_type = product_type
		
		assert isinstance(speed, float), 'speed not a float.'
		self.speed = speed
		
		assert isinstance(position, Vector2D), 'position not a Vector2D.'
		self.position = position
	
	def __repr__(self):
		return '<Factory, ID={0}, position={1}, speed={2}, product={3}>'.format(
			hex(id(self)), self.position, self.speed, self.product_type.name)

a = Factory(ProductType('Ziemiaciek', {}, 1), 1.04, Vector2D(10,10))
b = Factory(ProductType('Pluszowy Mort', {}, 1), 1.04, Vector2D(12,10))
