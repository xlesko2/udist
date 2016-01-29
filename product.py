from collections import deque

class ProductType(object):
	'''
	Class representing a product type.
	Product type specifies manufacture & transport requirements etc.
	'''
	name = 'ProductType'
	
	def __init__(self, name, requirements, difficulty):
		'''
		Params:
			-- name - string
			-- requirements - dict of required materials/products
			-- difficulty - float, affects rate of production
		'''
		assert str(name) == name, 'Product name not a string.'
		self.name = name
		
		assert isinstance(requirements, dict), 'Requirements not a dict.'
		assert all(isinstance(i, ProductType) for i in requirements),\
			'Invalid requirement (not a ProductType).'
		self.requirements = requirements
		
		assert isinstance(difficulty, float), 'Non-float difficulty ratio.'
		self.difficulty = difficulty
		return None
	
	def __repr__(self):
		return '<ProductType, ID={0}, name={1}, reqs={2}, difficulty={3}>'.format(
			hex(id(self)), self.name, self.requirements.keys(), self.difficulty)

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
	
	def __repr__(self):
		return '<Product, ID={0}, type={1}>'.format(hex(id(self)),
			self.product_type.name)

class Package(object):
	'''
	Class representing a package of products sent between Organizations.
	'''
	def __init__(self):
		self.products = deque()
		return None
	
	def size(self):
		return len(self.products)
	
	def pack(self, product):
		self.products.append(product)
		return None
	
	def unpack(self):
		assert len(self.products), 'Tried to unpack from empty Package {0}.'\
			.format(hex(id(self)))
		return self.products.popleft()
	
	def __repr__(self):
		return '<Package, ID={0}, products={1}'.format(hex(id(self)),
			list(self.products))
