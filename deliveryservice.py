class DeliveryService():

    def __init__(self, graph, history, orders, launchQueue, currentOrders, operator):
        self.graph = graph
        self.history = history
        self.orders = orders
        self.launchQueue = launchQueue
        self.currentOrders = currentOrders
        self.operator = operator

    def launchOrder(self, orderId):
        pass

    def addOrder(self):
        pass

    def deleteOrder(self, orderId):
        pass

    def getOrderInfo(self, orderId):
        pass

    def addItemToOrder(self, orderId, itemId):
        pass

    def deleteItemFromOrder(self, oderId, itemId):
        pass

    def buildRouteForOrder(self, orderId):
        pass

    def getLocation(self, orderId):
        pass

    def moveOrder(self, orderId):
        pass

    def confirmOrderTransition(self, orderId):
        pass

    def lookupHistory(self, orderId):
        pass