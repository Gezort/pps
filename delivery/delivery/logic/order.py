from datetime import datetime
from enum import Enum
from .list_items import ITEMS

class Criteria(Enum):
    time = 'time'
    cost = 'cost'

class Order():

    def __init__(self, id, time, items, route, start, end, error=False, error_no_items=False, cost=None, all_time=None, criteria=Criteria('time')):
        self.id = id
        self.creationTime = time
        self.itemList = items
        self.route = route
        self.criteria = criteria
        self.startLocation = start
        self.finishLocation = end
        self.cost = cost
        self.time = all_time
        self.error = error
        self.error_no_items = error_no_items

    def getLocation(self):
        return None if self.route is None else self.route.getCurrentLocation()

    def getLocationInfo(self):
        return None if self.route is None else self.route.getCurrentLocationInfo()

    def addItem(self, item_id):
        self.itemList.append(item_id)
    
    def atEnd(self):
        return self.getLocation() is None

    def deleteItem(self, item_id):
        if not item_id in self.itemList:
            return
        item_pos = 0
        for i in range(len(self.itemList)):
            if self.itemList[i] == item_id:
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
        return sum([ITEMS[id].getWeight() for id in self.itemList])

    def getCriteria(self):
        return self.criteria

    def setCriteria(self, criteria):
        self.criteria = criteria

    def getStartLocation(self):
        return self.startLocation

    def setStartLocation(self, start_location):
        self.startLocation = start_location

    def getFinishLocation(self):
        return self.finishLocation

    def setFinishLocation(self, value):
        self.finishLocation = value

    def setCost(self, cost):
        self.cost = cost

    def getCost(self):
        return self.cost

    def setTime(self, time):
        self.time = time

    def getTime(self):
        return self.time

    def __repr__(self):
        return "Order id = {} creationTime = {} \n route = {} startLocation = {}\
finishLocation = {} criteria = {}".format(self.id, self.creationTime,
                                                        self.route, self.startLocation,
                                                        self.finishLocation, self.criteria)
