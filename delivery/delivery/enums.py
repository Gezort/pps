from enum import Enum

class LegType(Enum):
    Sea = 'sea'
    Road = 'road'
    Air = 'air'

class OrderStatus(Enum):
    launched = 'launched'
    delivered = 'delivered'

class Criteria(Enum):
    time = 'time'
    cost = 'cost'