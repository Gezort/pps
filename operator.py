class Operator:
    def makeRoute(self, order, graph, flag):
        assert flag == "cost" or flag == "time"
        dist = {}
        marked = {}
        for edge in graph.getLegs():
            dist[edge.getFromId()] = None
            dist[edge.getToId()] = None
            marked[edge.getFromId()] = False
            marked[edge.getToId()] = False
        start = order.getStartLocation()
        dist[start] = 0
        fr = {}
        while True:
            chosen = None
            for key in d:
                if not mark[key] and (chosen is None or dist[key] < dist[chosen]):
                    chosen = key
            if chosen is None:
                break
            marked[chosen] = True
            for edge : graph.getNeighbours(chosen):
                u = edge.getToId()
                new_dist = dist[chosen] +
                    edge.getCost() if flag == "cost" else edge.getTime()
                if dist[u] is None or dist[u] > new_dist:
                    dist[u] = new_dist
                    fr[u] = edge
        cur = order.getFinishLocation()
        if dist[cur] is None:
            return None
        result = []
        while True:
            result.append(fr[cur])
            if cur == start:
                break
            cur = fr[cur].getFromId()
        return Route(reversed(result))

    def makeTimeOptimalRoute(self, order, graph):
        makeRoute(order, graph, "time") 
    def makeCostOptimalRoute(self, order, graph):
        makeRoute(order, graph, "cost")
