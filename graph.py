import pandas

class Graph:
    def getNeighbours(self, vertex):
        result = [edge for edge in self.legs if edge.getFromId() == vertex]
        return result
    def Graph(self):
        df = pandas.read_csv('graph.csv')
        self.legs = []
        for j in range(df):
            self.legs.append(
                Leg(df['id'][j],
                LegType(df['type'][j]),
                df['max_weight'][j],
                df['time'][j],
                df['cost'][j],
                df['from_id'][j],
                df['to_id'][j]))

