from vector2d import Vector2D
from product import ProductType
from organization import Organization, Mine, Factory, CustomerPoint
import random

class World(object):
	'''
	Class representing the game world (map).
	'''
	name = 'World'
	
	def __init__(self, size, objects):
		'''
		Params:
			-- size - Vector2D
			-- objects - dict of Organization objects (subject to extension
				to other classes later in the development).
		'''
		assert isinstance(size, tuple) and len(size) == 2, 'size not a 2-tuple.'
		self.size = Vector2D(*size)
		
		assert isinstance(objects, list)
		self.objects = dict()
		
		# material production factory database (for supply purposes)
		self.product_origin = dict()
		
		for obj in objects:
			assert isinstance(obj, Organization),\
				'{0} not an organization object.'.format(obj)
			assert obj.position.x in range(self.size.x)\
				and obj.position.y in range(self.size.y),\
				'{0} outside of world (size {1})'.format(
					obj.position, self.size)
			assert not(obj.position in self.objects), '{0} occupied by {1}'\
				.format(obj.position, '{0} (ID {1})'.format(
					self.objects[obj.position].__class__.name,
					hex(id(self.objects[obj.position]))))
			self.objects[obj.position] = obj
			if isinstance(obj, Factory) or isinstance(obj, Mine):
				self.product_origin[obj.product_type] = obj
			
		for i in self.objects:
			if isinstance(self.objects[i], Factory) or\
				isinstance(self.objects[i], CustomerPoint):
				self.objects[i].update_suppliers(self)
		
		self.map = self.construct_map()
		return None
	
	
	def __repr__(self):
		return '<World {0}, size {1}, objects {2}>'.format(hex(id(self))[-5:],
			self.size, [str(i) for i in self.objects.values()])
	def __str__(self):
		return 'World object\nSize: {0}x{1} tiles\nObjects:{2}'.format(
			self.size.x, self.size.y, '\n' + '\n'.join(['{0} at {1}'.format(
			str(v),str(k)) for k,v in self.objects.items()]))
	
	def single_round(self, capacity_variation):
		for obj in self.objects.values():
			if capacity_variation != 0:
				temp_capacity = int(obj.capacity + random.choice([-1,1]) *\
					random.random() * (obj.capacity * capacity_variation))
			obj.single_round(temp_capacity)
		return None
	
	def construct_map(self):
		map_matrix = [[' ' for j in range(self.size.y)] for i in range(self.size.x)]
		for obj in self.objects:
			if isinstance(self.objects[obj], Mine):
				map_matrix[obj.x][obj.y] = 'M'
			elif isinstance(self.objects[obj], Factory):
				map_matrix[obj.x][obj.y] = 'F'
			elif isinstance(self.objects[obj], CustomerPoint):
				map_matrix[obj.x][obj.y] = 'C'
		return '\n'.join([' '.join(i) for i in map_matrix])
