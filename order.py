from datetime import datetime

class Order():

    STATUS = {0 : 'launched', 1 : 'delivered'}
    CRITERIA = {0 : 'time', 1 : 'cost'}

    def __init__(self, id, time, items, route, start, end, criteria=0):
        self.id = id
        self.creationTime = time
        self.itemList = items
        self.route = route
        self.status = 0
        self.criteria = criteria
        self.startLocation = start
        self.finishLocation = end

    def getLocation(self):
        return self.route.getCurrentLocation()

    def addItem(self, item):
        self.itemList.append(item)

    def deleteItem(self, item):
        item_pos = 0
        for i in range(len(self.itemList)):
            if self.itemList[i] == item:
                item_pos = i
                break
        self.itemList = self.itemList[:item_pos] + self.itemList[item_pos + 1:]

    def getItemsList(self):
        return self.itemList

    def getRoute(self):
        return self.route

    def setRoute(self, route):
        self.route = route

    def move(self):
        self.route.move()