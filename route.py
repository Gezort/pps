from leg import Leg

class Route():

    def __init__(self, legs, location=0):
        self.listLegs = legs
        self.currentLocation = location

    def getCurrentLocation():
        return self.listLegs[self.currentLocation]

    def move():
        self.currentLocation += 1

    def __repr__(self):
        return str([edge.getId() for edge in self.listLegs])

    def getLegsIds(self):
        return [edge.getId() for edge in self.listLegs]
