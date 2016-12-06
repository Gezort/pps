from .oper import Operator
from .order import Order
from .warehouse import Warehouse
from .orders_queue import OrdersQueue

class DeliveryService:

    def __init__(self, graph):
        self.graph = graph
        self.orders_dict = {}
        self.orders_cnt = 0
        self.orders_queue = OrdersQueue()
        self.warehouse = Warehouse()

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
        print("MOCK transferHistory for order_id = {}".format(order_id))

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
        # self.current_history.delete(order_id)

    def launchOrder(self, order_id):
        print (self.orders_dict)
        if not self.warehouse.checkItems(
                self.orders_dict[order_id].getItemsList()):
            return False
        self.buildRouteForOrder(order_id)
        self.orders_queue.push(self.orders_dict[order_id])
        return True

    def moveOrder(self, order_id):
        self.orders_dict[order_id].move()
        if self.orders_dict[order_id].atEnd():
            self.transferHistory(order_id)
            self.deleteOrder(order_id)
        
    def reportFail(self, order_id, change_available):
        if change_available:
            self.orders_dict[order_id].setStartLocation(
                    self.orders_dict[order_id].getLocation().getFromId())
            self.buildRouteForOrder(order_id)

