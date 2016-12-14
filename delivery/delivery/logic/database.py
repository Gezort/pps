class Database():

    def __init__(self):
        self.storage = dict()

    def add(self, orderId, timestamp, leg):
        if orderId not in self.storage:
            self.storage[orderId] = []
        self.storage[orderId].append((timestamp, leg))            

    def query(self, orderId, beginTime, endTime):
        print (orderId, beginTime, endTime)
        print (self.storage)
        return [(orderId, val[0], val[1]) for val in self.storage[orderId] if val[0] >= beginTime and val[0] <= endTime]

    def delete(self, orderId):
        self.storage[orderId] = []