import pandas
from .leg import Leg, LegType

class Graph:
    
    def getNeighbours(self, vertex, max_weight):
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
        print("edges:")
        for edge in self.legs:
            print(repr(edge))
    def getLegs(self):
        return self.legs

