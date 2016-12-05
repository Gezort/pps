class OrdersQueue:
    def __init__(self):
        self.queue = []
    def push(self, order):
        self.queue.append(order)
        self.pop()
    def pop(self):
        print("OrdersQueue.pop order = {}".format(self.queue[0]))
        self.queue = self.queue[1:]
