from enum import Enum

class LegType(Enum):
    Sea = 'sea'
    Road = 'road'
    Air = 'air'

class Leg:
    def __init__(self, id, type, max_weight, time, cost, from_id, 
        from_name, to_id, to_name, name):
        self.id = id
        self.type = type
        self.maxWeight = max_weight
        self.time = time
        self.cost = cost
        self.fromId = from_id
        self.toId = to_id
        self.name = name
        self.fromName = from_name
        self.toName = to_name

        
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

    def getFromName(self):
        return self.fromName

    def getToId(self):
        return self.toId

    def getToName(self):
        return self.toName

    def getId(self):
        return self.id

    def getName(self):
        return self.name
