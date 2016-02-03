from organization import Mine, Factory, CustomerPoint
from product import ProductType
from vector2d import Vector2D
from world import World
from matplotlib import pyplot

textile = ProductType('Textile', {}, 0.97)
ziemiaciek = ProductType('Ziemiaciek', {textile: 2}, 1.04)
pluszowy_mort = ProductType('Pluszowy Mort', {textile: 2, ziemiaciek: 1}, 1.24)
m_tex = Mine(textile, 1000, Vector2D(5,5))
f_ziem = Factory(ziemiaciek, 400, Vector2D(7,12))
f_mort = Factory(pluszowy_mort, 1500, Vector2D(15,7))
c_mort = CustomerPoint(pluszowy_mort, 500, Vector2D(4,18))
w = World((20,20), [m_tex, f_ziem, f_mort, c_mort])

class Simulation(object):
	'''
	Top-level runtime class. Works with a World object, runs simulations
	and provides graphs/plots of statistical outputs.
	'''
	def __init__(self, world):
		'''
		Param world - world Object ref
		'''
		assert isinstance(world, World), 'world not a World instance.'
		self.world = world
		
		self.plot_data = dict()
		for obj in self.world.objects.values():
			self.plot_data[obj] = list()
		
		self.age = 0 # simulation age (in time units)
		return None
	
	def simulate(self, rounds):
		for i in range(rounds):
			w.single_round()
			self.age += 1
			for obj in self.plot_data:
				if isinstance(obj, CustomerPoint):
					self.plot_data[obj].append(sum(obj.storage.values()))
				else:
					self.plot_data[obj].append(obj.production)
		return None

	def create_plot(self):
		legends = list()
		for obj in self.plot_data:
			pyplot.plot([i+1 for i in range(self.age)], self.plot_data[obj])
			legends.append('{0} {1}'.format(obj.name, hex(id(obj))[-5:]))
		pyplot.legend(legends)
		pyplot.title('World {0} (sim age: {1} rounds) performance stats'.format(
			hex(id(self.world))[-5:], self.age))
		pyplot.show()

sim = Simulation(w)
