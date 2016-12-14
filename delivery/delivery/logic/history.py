from .database import Database

class OrdersHistory():
    
    def __init__(self):
        self.database = Database()

    def add(self, orderId, timestamp, leg):
        print("Added to history:(%s;%s;%s)" % (orderId, timestamp, leg))
        self.database.add(orderId, timestamp, leg)

    def query(self, orderId, beginTime, endTime):
        return self.database.query(orderId, beginTime, endTime)


class CurrentOrdersHistory(OrdersHistory):
    
    def delete(self, orderId): 
        self.database.delete(orderId)
