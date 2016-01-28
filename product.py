class ProductType(object):
	'''
	Class representing a product type.
	Product type specifies manufacture & transport requirements etc.
	'''
	name = 'ProductType'
	
	def __init__(self, name, requirements, production_time):
		'''
		Params:
			-- name - string
			-- requirements - dict of required materials/products
			-- production_time - base time of making a product of this type
				(integer value)
		'''
		assert str(name) == name, 'Product name not a string.'
		self.name = name
		
		assert isinstance(requirements, dict), 'Requirements not a dict.'
		assert all(isinstance(i, Product) for i in requirements),\
			'Invalid requirement (not a product).'
		self.requirements = requirements
		
		assert isinstance(production_time, int), 'Non-integer production time.'
		self.production_time = production_time
		return None


class Product(object):
	'''
	Class representing a single product.
	A product is an instance of a product type
	(though this is not represented by object organization here).
	'''
	name = 'Product'
	
	def __init__(self, product_type):
		'''
		Params:
			-- product_type - ProductType object ref.
		'''
		assert isinstance(product_type, ProductType),\
			'product_type not ProductType'
		self.product_type = product_type
		return None
