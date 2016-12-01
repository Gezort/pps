from leg import Leg

class Route():

    def __init__(self, legs, location):
        self.listLegs = legs
        self.currentLocation = location

    def getCurrentLocation():
        return self.listLegs[self.currentLocation]

    def move():
        self.currentLocation += 1