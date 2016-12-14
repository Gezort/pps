from .oper import Operator
from .order import Order
from .warehouse import Warehouse
from .orders_queue import OrdersQueue
from .history import OrdersHistory, CurrentOrdersHistory

import time

class DeliveryService:

    def __init__(self, graph):
        self.graph = graph
        self.orders_dict = {}
        self.orders_cnt = 0
        self.orders_queue = OrdersQueue()
        self.warehouse = Warehouse()
        self.history = OrdersHistory()
        self.current_history = CurrentOrdersHistory()

    def getOrderInfo(self, order_id):
        return self.orders_dict[order_id].getCurrentLeg()

    def addItemToOrder(self, order_id, item_id):
        self.orders_dict[order_id].addItem(item_id)

    def deleteItemFromOrder(self, order_id, item_id):
        self.orders_dict[order_id].deleteItem(item_id)

    def buildRouteForOrder(self, order_id):
        route = Operator().makeRoute(self.orders_dict[order_id], self.graph)
        self.orders_dict[order_id].setRoute(route)

    def getLocation(self, order_id):
        return self.orders_dict[order_id].getLocation()

    def transferHistory(self, order_id):
        print ("Transfer history")
        entries = self.current_history.query(order_id, 0, time.time())
        for entry in entries:
            self.history.add(entry[0], entry[1], entry[2])
        print("MOCK transferHistory for order_id = {}".format(order_id))
        print("HISTORY:", self.history)

    def setStartLocation(self, order_id, start_location):
        assert order_id in self.orders_dict
        self.orders_dict[order_id].setStartLocation(start_location)

    def setFinishLocation(self, order_id, finish_location):
        assert order_id in self.orders_dict
        self.orders_dict[order_id].setFinishLocation(finish_location)

    def setCriteria(self, order_id, criteria):
        self.orders_dict[order_id].setCriteria(criteria)

    def getCriteria(self, order_id):
        return self.orders_dict[order_id].getCriteria()

    # methods for order lifecycle
    def addOrder(self):
        self.orders_dict[self.orders_cnt] = Order(self.orders_cnt, "timestamp",
                [], None, None, None)
        self.orders_cnt += 1
        return self.orders_cnt - 1
    
    def deleteOrder(self, order_id):
        del self.orders_dict[order_id]
        self.current_history.delete(order_id)

    def launchOrder(self, order_id):
        print (self.orders_dict)
        if not self.warehouse.checkItems(
                self.orders_dict[order_id].getItemsList()):
            return False
        self.buildRouteForOrder(order_id)
        self.orders_queue.push(self.orders_dict[order_id])
        return True

    def moveOrder(self, order_id):
        self.current_history.add(order_id, time.time(), self.getLocation(order_id).getId())
        print("actually added")
        self.orders_dict[order_id].move()
        
        if self.orders_dict[order_id].atEnd():
            self.transferHistory(order_id)
            self.deleteOrder(order_id)
        
    def reportFail(self, order_id, change_available):
        if change_available:
            self.orders_dict[order_id].setStartLocation(
                    self.orders_dict[order_id].getLocation().getFromId())
            self.buildRouteForOrder(order_id)

