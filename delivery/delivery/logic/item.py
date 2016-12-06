class Item():

    def __init__(self, id, weight, name, cost):
        self.id = id
        self.weight = weight
        self.name = name
        self.cost = cost

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getCost(self):
        return self.cost

    def __repr__(self):
        return 'Item. name: %s, weight: %.3f, cost: %.3f' % (self.name, self.weight, self.cost)