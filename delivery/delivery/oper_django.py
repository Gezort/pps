from models import Order, Leg, Route

class Operator:
    def makeRoute(self, orderId):
        order = Order.objects.filter(id=orderId)[0]
        print(order.criteria)
        dist = {}
        marked = {}

        for edge in Leg.objects.all():
            dist[edge.fromLocation] = None
            dist[edge.toLocation] = None
            marked[edge.fromLocation] = False
            marked[edge.toLocation] = False

        start = order.startLocation
        print("makeRoute start = {}".format(start))
        dist[start] = 0
        fr = {}

        while True:
            chosen = None
            for key in dist:
                if not marked[key] and dist[key] is not None and \
                        (chosen is None or dist[key] < dist[chosen]):
                    chosen = key
            print("chosen = {}".format(chosen))
            if chosen is None:
                break
            marked[chosen] = True
            for edge in Leg.objects.filter(fromLocation=chosen, maxWeight__gte=order.getWeight()):
                print("edge {}".format(edge.id))
                u = edge.toLocation
                new_dist = dist[chosen] + \
                    edge.cost if order.criteria == "cost" else edge.time
                if dist[u] is None or dist[u] > new_dist:
                    dist[u] = new_dist
                    fr[u] = edge

        cur = order.finishLocation
        if dist[cur] is None:
            return None
        print("dist {}".format(dist[cur]))
        result = []
        while True:
            if cur == start:
                break
            result.append(fr[cur])
            cur = fr[cur].getFromId()
        #return Route(result[::-1])
