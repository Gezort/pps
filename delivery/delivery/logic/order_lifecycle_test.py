from .delivery_service import DeliveryService
from .graph import Graph
from .item import Item
from .order import Criteria

graph = Graph()
ds = DeliveryService(graph)
order_id = ds.addOrder()
print("order_id = {}".format(order_id))
ds.setStartLocation(order_id, 0)
ds.setFinishLocation(order_id, 2)
item1 = Item(4, "chma", 15)
ds.addItemToOrder(order_id, item1)
print(ds.orders_dict[order_id])
ds.launchOrder(order_id)
print(ds.orders_dict[order_id].getRoute())
print(ds.orders_dict[order_id].getLocation())
ds.moveOrder(order_id)
print(ds.orders_dict[order_id].getLocation())
ds.moveOrder(order_id)
assert order_id not in ds.orders_dict

order_id = ds.addOrder()
print("order_id = {}".format(order_id))
ds.setStartLocation(order_id, 0)
ds.setFinishLocation(order_id, 2)
item1 = Item(4, "chma", 15)
ds.addItemToOrder(order_id, item1)
print(ds.orders_dict[order_id])
ds.launchOrder(order_id)
print(ds.orders_dict[order_id].getRoute())
print(ds.orders_dict[order_id].getLocation())
ds.moveOrder(order_id)
print(ds.orders_dict[order_id].getLocation())
ds.setCriteria(order_id, Criteria("cost"))
print(ds.getCriteria(order_id))
ds.reportFail(order_id, True)
print(ds.orders_dict[order_id].getLocation())
ds.moveOrder(order_id)
assert order_id not in ds.orders_dict
