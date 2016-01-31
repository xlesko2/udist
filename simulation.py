from organization import Mine, Factory, CustomerPoint
from product import ProductType
from vector2d import Vector2D
from world import World

textile = ProductType('Textile', {}, 0.97)
ziemiaciek = ProductType('Ziemiaciek', {textile: 2}, 1.04)
pluszowy_mort = ProductType('Pluszowy Mort', {textile: 2, ziemiaciek: 1}, 1.24)
m_tex = Mine(textile, 1000, Vector2D(5,5))
f_ziem = Factory(ziemiaciek, 400, Vector2D(7,12))
f_mort = Factory(pluszowy_mort, 1500, Vector2D(15,7))
c_mort = CustomerPoint(pluszowy_mort, 500, Vector2D(4,18))
w = World((20,20), [m_tex, f_ziem, f_mort, c_mort])
