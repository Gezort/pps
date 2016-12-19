import pandas
from .leg import Leg, LegType
from collections import namedtuple


DestPoint = namedtuple("DestPoint", ["id", "name"])

class Graph:
    
    def getNeighbours(self, vertex, max_weight=1e18):
        result = [edge for edge in self.legs if edge.getFromId() == vertex and
                edge.getMaxWeight() >= max_weight]
        return result

    def __init__(self):
        df = pandas.read_csv('./delivery/logic/graph.csv')
        df_nodes = pandas.read_csv('./delivery/logic/nodes.csv')
        self.legs = []
        for j in range(len(df)):
            self.legs.append(
                Leg(df['id'][j],
                LegType(df['type'][j]),
                df['max_weight'][j],
                df['time'][j],
                df['cost'][j],
                df['from_id'][j],
                df_nodes['name'][df['from_id'][j]],
                df['to_id'][j],
                df_nodes['name'][df['to_id'][j]],
                df['name'][j]
            ))

    def getLegs(self):
        return self.legs

    def getLegsWithName(self):
        names = [DestPoint(id=leg.getId(), name=leg.getName()) 
                 for leg in self.legs]
        return names


    def getReachableNodes(self, node):
        order = [node]
        result = [node]
        while len(order) > 0:
            v = order[0]
            order = order[1:]
            for edge in self.getNeighbours(v):
                u = edge.getToId()
                if u not in result:
                    order.append(u)
                    result.append(u)
        return result
