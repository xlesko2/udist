class Organization(object):
	'''
	Class representing a 'place' in the world, such as a factory or store.
	Virtual class inherited by Factory.
	'''
	pass

class Factory(Organization):
	'''
	Class representing a single manufacturing unit.
	The factory is placed on a certain position in the game world,
	and manufactures a product based on its specification.
	'''
	def __init__(self, product_data, position):
		'''
		Params:
			-- product_data - dictionary of data. So far, not sure which
			-- position - 2D Vector that positions factory in game world
		'''
		pass
