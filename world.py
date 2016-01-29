from vector2d import Vector2D
from product import ProductType
from organization import Organization, Factory

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
			if isinstance(obj, Factory):
				self.product_origin[obj.product_type] = obj
			
		for i in self.objects:
			if isinstance(self.objects[i], Factory):
				self.objects[i].update_suppliers(self)
		return None
	
	def single_round(self):
		for obj in self.objects:
			self.objects[obj].single_round()
	
	def print_map(self):
		map_matrix = [['_' for j in range(self.size.y)] for i in range(self.size.x)]
		for obj in self.objects:
			if isinstance(self.objects[obj], Factory):
				map_matrix[obj.x][obj.y] = 'F'
		for i in map_matrix:
			print(i)
		return None
	
	def __repr__(self):
		return '<World, ID={0}, size={1}, objects=[{2}]>'.format(
			hex(id(self)), self.size, ', '.join(['{0} at {1}'.format(
				'{0} (ID {1})'.format(self.objects[key].__class__.name,
					hex(id(self.objects[key]))), key) for key in self.objects]))
	
	def __str__(self):
		return 'World object\nSize: {0}x{1} tiles\nObjects:{2}'.format(
			self.size.x, self.size.y, '\n' + '\n'.join(['{0} at {1}'.format(
			str(v),str(k)) for k,v in self.objects.items()]))

textile = ProductType('Textile', {}, 0.97)
ziemiaciek = ProductType('Ziemiaciek', {textile: 2}, 1.04)
pluszowy_mort = ProductType('Pluszowy Mort', {textile: 2, ziemiaciek: 1}, 1.24)
f_tex = Factory(textile, 1000, Vector2D(5,5))
f_ziem = Factory(ziemiaciek, 400, Vector2D(7,12))
f_mort = Factory(pluszowy_mort, 1500, Vector2D(15,7))
w = World((20,20), [f_tex, f_ziem, f_mort])
