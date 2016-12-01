class Item():

    def __init__(self, weight, name, cost):
        self.weight = weight
        self.name = name
        self.cost = cost

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getCost(self):
        return self.cost

    def __str__(self):
        return 'Item. name: %s, weight: %.3f, cost: %.3f' % (self.name, self.weight, self.cost)