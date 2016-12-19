import pandas
from .leg import Leg, LegType
from collections import namedtuple


Node = namedtuple("Node", ["id", "name"])

class Graph:
    
    def getNeighbours(self, vertex, max_weight=1e-18):
        result = [edge for edge in self.legs if edge.getFromId() == vertex and
                edge.getMaxWeight() >= max_weight]
        return result

    def __init__(self):
        df = pandas.read_csv('./delivery/logic/graph.csv')
        df_nodes = pandas.read_csv('./delivery/logic/nodes.csv')
        self.nodes_for_templ = []
        self.nodes = {}
        for i in range(len(df_nodes)):
            self.nodes_for_templ.append(Node(id=df_nodes['id'][i], 
                              name=df_nodes['name'][i]))
            self.nodes[df_nodes['id'][i]] = df_nodes['name'][i]
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
        # names = [Node(id=leg.getFromId(), name=leg.getFromName()) 
                 # for leg in self.legs]
        # return names
        return self.nodes_for_templ

    def getReachableNodes(self, node):
        order = [node]
        result = [node]
        print(self.getNeighbours(node))
        names = [Node(id = node, name = self.nodes[node])]
        while len(order) > 0:
            v = order[0]
            order = order[1:]
            for edge in self.getNeighbours(v):
                u = edge.getToId()
                if u not in result:
                    order.append(u)
                    result.append(u)
                    names.append(Node(id=u, name=self.nodes[u]))
        print(result)
        return names