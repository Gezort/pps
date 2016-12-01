from datetime import datetime
from enum import Enum

class OrderStatus(Enum):
    launched = 'launched'
    delivered = 'delivered'

class Criteria(Enum):
    time = 'time'
    cost = 'cost'

class Order():

    def __init__(self, id, time, items, route, start, end, criteria=Criteria('time')):
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

    def getWeight(self):
        return sum([item.getWeight() for item in self.itemList])

    def getCriteria(self):
        return self.criteria

    def getStartLocation(self):
        return self.startLocation

    def getFinishLocation(self):
        return self.finishLocation

    def __repr__(self):
        return "Order id = {} creationTime = {} \n route = {} startLocation = {}\
                finishLocation = {} criteria = {}".format(self.id, self.creationTime,
                    self.route, self.startLocation,
                    self.finishLocation, self.criteria)
