from graph import Graph
from item import Item
from order import Order
from oper import Operator
#from leg import Leg

g = Graph()
items = [Item(4, "chma", 15), Item(5, "chma2", 10)]
for item in items:
    print(item)
order = Order(0, 0, items, None, 0, 2)
op = Operator()
route = op.makeRoute(order, g)
print(route)
