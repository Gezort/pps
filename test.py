from graph import Graph
from item import Item
from order import Order, Criteria
from oper import Operator
#from leg import Leg

g = Graph()
items = [Item(4, "chma", 15), Item(5, "chma2", 10)]
for item in items:
    print(item)
order = Order(0, 0, items, None, 0, 2)
op = Operator()
route = op.makeRoute(order, g)
assert route.getLegsIds() == [0, 1]

order2 = Order(0, 0, items, None, 0, 2, Criteria("cost"))
route2 = op.makeRoute(order2, g)
print(route2.getLegsIds())
assert route2.getLegsIds() == [2]
