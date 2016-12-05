from .order import Criteria
from .route import Route

class Operator:
    def makeRoute(self, order, graph):
        dist = {}
        marked = {}
        for edge in graph.getLegs():
            dist[edge.getFromId()] = None
            dist[edge.getToId()] = None
            marked[edge.getFromId()] = False
            marked[edge.getToId()] = False
        start = order.getStartLocation()
        print("makeRoute start = {}".format(start))
        dist[start] = 0
        fr = {}
        while True:
            chosen = None
            for key in dist:
                if not marked[key] and dist[key] is not None and (chosen is None or dist[key] < dist[chosen]):
                    chosen = key
            print("chosen = {}".format(chosen))
            if chosen is None:
                break
            marked[chosen] = True
            for edge in graph.getNeighbours(chosen, order.getWeight()):
                print("edge {}".format(edge))
                u = edge.getToId()
                new_dist = dist[chosen] + \
                    edge.getCost() if order.getCriteria() == Criteria("cost") else edge.getTime()
                if dist[u] is None or dist[u] > new_dist:
                    dist[u] = new_dist
                    fr[u] = edge
        cur = order.getFinishLocation()
        if dist[cur] is None:
            return None
        print("dist {}".format(dist[cur]))
        result = []
        while True:
            if cur == start:
                break
            result.append(fr[cur])
            cur = fr[cur].getFromId()
        return Route(result[::-1])

    def makeTimeOptimalRoute(self, order, graph):
        makeRoute(order, graph, "time") 
    def makeCostOptimalRoute(self, order, graph):
        makeRoute(order, graph, "cost")
