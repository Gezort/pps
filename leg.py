from enum import Enum

class LegType(Enum):
    Sea = 'sea'
    Road = 'road'

class Leg:
    def Leg(self, id, type, max_weight, time, cost, from_id, to_id):
        self.id = id
        self.type = type
        self.max_weight = max_weight
        self.time = time
        self.cost = cost
        self.from_id = from_id
        self.to_id = to_id
    def getType(self):
        return self.type
    def getTime(self):
        return self.time
    def getCost(self):
        return self.cost
    def getMaxWeight(self):
        return self.maxWeight
    def getFromId(self):
        return self.fromId
    def getToId(self):
        return self.toId
    def getId(self):
        return self.id
