from enum import Enum

class LegType(Enum):
    Sea = 'sea'
    Road = 'road'

class Leg:
    def __init__(self, id, type, max_weight, time, cost, from_id, to_id):
        self.id = id
        self.type = type
        self.maxWeight = max_weight
        self.time = time
        self.cost = cost
        self.fromId = from_id
        self.toId = to_id
    def __repr__(self):
        return "Leg id = {} type = {} max_weight = {} time = {} cost = {} from_id = {} to_id = {}".format(self.id, self.type, self.maxWeight,
                self.time, self.cost,
                self.fromId, self.toId)

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
