from product import ProductType, Product, Package
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
		
		# list of factories supplying the materials
		self.suppliers = dict()
		
		# supply input queue
		self.input = deque()
		
		# list of customers for products
		self.customers = dict()
		
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
	
	def update_suppliers(self, world):
		'''
		Method for updating the refs to factories supplying required materials.
		Param world -- ref to world object
		'''
		for m in self.storage:
			self.suppliers[m] = world.product_origin[m]
		return None
	
	def material_sufficient(self):
		'''
		Aux. method returning the number of product items that could
		be produced with current materials in storage (not taking into account
		the capacity of the factory).
		'''
		return int(min([self.storage[i]/self.product_type.requirements[i]\
			for i in self.storage]))
	
	def accept_supplies(self):
		'''
		Method for accepting the supplies, i.e. moving them from the first
		place in input queue into the storage.
		'''
		if len(self.input) == 0: # no supplies available
			 return None
		incoming_load = self.input.popleft()
		for package in incoming_load:
			while package.size() > 0:
				item = package.unpack
				assert item in self.storage, 'Accepted spam package.'
				self.storage[item] += 1
		return None
		
	def produce(self):
		'''
		Method for handling producing during one time unit.
		'''
		amount = min([self.material_sufficient(), self.capacity])
		for item in self.product_type.requirements:
			self.storage[item] -= amount * self.product_type.requirements[item]
		for p in range(amount):
			self.output.append(Product(self.product_type))
		return None
	
	def send(self, package, customer):
		dist = int((self.position - customer.position).length)
		while len(customer.input) < dist:
			customer.input.append(list())
		customer.input[dist - 1].append(package)
		return None
	def export(self):
		'''
		Method handling production export to customers.
		Current system: production is divided among customers in ratios
		equivalent to their product requirements.
		'''
		total_requirements = sum(self.customers.values())
		production_available = len(self.output)
		for cust in self.customers:
			package = Package()
			for i in range(int(production_available * \
				self.customers[cust]/total_requirements)):
				package.pack(self.output.popleft())
			self.send(package, cust)
		return None
	
ziemiaciek = ProductType('Ziemiaciek', {}, 1.00)
a = Factory(ziemiaciek, 220, Vector2D(10,10))
b = Factory(ProductType('Pluszowy Mort', {ziemiaciek: 100}, 1.02), 470, Vector2D(12,10))
