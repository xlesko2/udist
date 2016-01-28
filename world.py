from vector2d import Vector2D

class World(object):
	'''
	Class representing the game world (map).
	'''
	def __init__(self, size, objects = dict()):
		'''
		Params:
			-- size - a Vector2D
			-- objects - a dict with objects as keys and coordinates as values.
			The world.objects dictionary reverses these pairs.
		'''
		self.size = Vector2D(*size)
		self.objects = dict()
		for ref in objects:
			assert objects[ref].x < self.size.x\
				and objects[ref].y < self.size.y,\
				'Object placed outside of the world.'
			self.objects[objects[ref]] = ref
		return None
	
	def __str__(self):
		return 'World object\nSize: {0}x{1} tiles\nObjects:{2}'.format(
			self.size.x, self.size.y, '\n' + '\n'.join(['{0} at {1}'.format(
			str(v),str(k)) for k,v in self.objects.items()]))

w = World((42,69), {'Dante': Vector2D(41,68)})
