from vector2d import Vector2D
from organization import Organization, a, b

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

w = World((42,69), [a,b])
