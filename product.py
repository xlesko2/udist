from product_type import ProductType
from organization import Organization

class Product(object):
	'''
	Class representing a single product.
	A product is an instance of a product type
	(though this is not represented by object organization here).
	'''
	def __init__(self, product_type, holder):
		'''
		Params:
			-- product_type - ProductType object ref.
			-- holder - Organization object ref.
		'''
		assert isinstance(product_type, ProductType),\
			'product_type not ProductType'
		self.product_type = product_type
		assert isinstance(holder, Organization),\
			'Holder not an Organization object.'
		self.holder = holder
		return None
