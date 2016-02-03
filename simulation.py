from organization import Mine, Factory, CustomerPoint
from product import ProductType
from vector2d import Vector2D
from world import World
from matplotlib import pyplot

silicone = ProductType('Silicone', {}, 1.0)
plastic = ProductType('Plastic', {}, 1.2)
aluminium = ProductType('Aluminium', {}, 1.1)
processor = ProductType('Processor', {silicone: 8}, 3.2)
ram = ProductType('RAM', {silicone: 4, plastic: 2}, 1.8)
gpu = ProductType('GPU', {silicone: 7}, 3.3)
case = ProductType('PC Case', {aluminium: 12, plastic: 4}, 1.2)
computer = ProductType('Computer', {processor: 1, ram: 4, gpu: 1, case: 1}, 2.7)

m_sil = Mine(silicone, 1200, Vector2D(1,1))
m_plast = Mine(plastic, 1400, Vector2D(14,0))
m_alu = Mine(aluminium, 1500, Vector2D(15,14))
f_proc = Factory(processor, 700, Vector2D(7,2))
f_ram = Factory(ram, 1200, Vector2D(8,4))
f_gpu = Factory(gpu, 800, Vector2D(6,3))
f_case = Factory(case, 1400, Vector2D(1,6))
f_comp = Factory(computer, 1000, Vector2D(4,12))
c_comp = CustomerPoint(computer, 1400, Vector2D(19,17))

w = World((20,20), [m_sil, m_plast, m_alu, f_proc, f_ram, f_gpu, f_case,
	f_comp, c_comp])

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
		for obj in sorted(self.plot_data,\
			key = lambda i: super(type(i), i).inher_order.index(i.name)):
			pyplot.plot([i+1 for i in range(self.age)], self.plot_data[obj])
			legends.append('{0} {1} ({2})'.format(
				obj.name, hex(id(obj))[-5:], obj.product_type.name))
		pyplot.legend(legends)
		pyplot.title('World {0} (sim age: {1} rounds) performance stats'.format(
			hex(id(self.world))[-5:], self.age))
		pyplot.show()
		return None


sim = Simulation(w)
