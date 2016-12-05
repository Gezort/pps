class Database():

    def __init__(self):
        self.storage = dict()

    def add(self, orderId, timestamp, leg):
        if orderId in self.storage:
            self.storage[orderId] = []
        self.storage[orderId].append((timestamp, leg))            

    def queue(self, orderId, beginTime, endTime):
        return [val for val in self.storage[orderId] if val[0] >= beginTime and val[0] <= endTime]

    def delete(self, orderId):
        self.storage[orderId] = []