from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_GET, require_POST
from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied, ImproperlyConfigured, ObjectDoesNotExist
from .forms import OrderIdForm, ConfigureOrderForm
from .logic.delivery_service import DeliveryService
from .logic.graph import Graph
from .logic.item import Item
from .logic.order import Criteria
from .logic.list_items import ITEMS 
from functools import wraps
import networkx as nx
import matplotlib.pyplot as plt
import datetime

DELIVERY_SERVICE = DeliveryService(Graph())

@wraps
def shows_error(func):
    def decorated(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return HttpResponse(str(e))

def check_user(request, group, name=None):
    print(name)
    user = request.user
    print(user.username)
    if  user is None or (not user.is_authenticated()) or str(user.groups.all()[0]) != group:
        raise PermissionDenied("You can't access this page")
    if name is not None and user.username != name:
        raise PermissionDenied(name)

@shows_error
@require_GET
def index(request):
    return render(request, 'index.html')


@shows_error
@require_GET
def homepage(request):
    user = request.user
    if  user is None or (not user.is_authenticated()):
        raise PermissionDenied("You aren't authenticated")
    context={'is_courier' : str(request.user.groups.all()[0]) == 'couriers'}
    return render(request, 'homepage.html', context=context)

@shows_error
@require_GET
def create(request):
    check_user(request, 'users')
    global DELIVERY_SERVICE
    order_id = DELIVERY_SERVICE.addOrder()
    return render(request, 'create_order.html', {'id' : order_id})

@shows_error
@require_POST
def delete(request):
    id = int(request.POST['order_id'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.deleteOrder(id)    
    # return render(request, 'delete_order.html', {'id' : id})
    return redirect(reverse(homepage)) 

@shows_error
@require_POST
def launch(request):
    id = int(request.POST['order_id'])
    global DELIVERY_SERVICE
    launched = DELIVERY_SERVICE.launchOrder(id)
    # return render(request, 'launch_order.html', {'launched' : launched})
    return redirect(reverse(homepage))

@shows_error
def track(request):
    check_user(request, 'users')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            try:
                global DELIVERY_SERVICE
                location = DELIVERY_SERVICE.getLocation(id)
                if location is None:
                    raise Http404("Order ID not found")
                return render(request, 'track_order.html', {'location' : location.getId(), 
                    'order_id': id})
            except:
                raise Http404("Order ID not found")    
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})

@shows_error
@require_POST
def configure(request):
    # check_user(request, 'users')
    # if request.method == 'POST':
    #     form = OrderIdForm(request.POST)
    #     if form.is_valid():
    #         id = int(form.cleaned_data['id'])
    #         return redirect(reverse(configure_order, kwargs={'id' : id}))
    # else:
    #     form = OrderIdForm()
    # return render(request, 'input_order_id.html', {'form' : form})
    
    id = int(request.POST['order_id'])
    return redirect(reverse(configure_order, kwargs={'id' : id}))

@shows_error
def configure_order(request, id):
    check_user(request, 'users')
    global DELIVERY_SERVICE
    global ITEMS
    if int(id) not in DELIVERY_SERVICE.orders_dict:
        raise Http404("Order ID not found")

    nodes = DELIVERY_SERVICE.getGraph().getLegsWithName()
    order = DELIVERY_SERVICE.orders_dict[int(id)]
    items = order.itemList
    route = order.route
    criteria = 'time' if order.criteria == Criteria.time else 'cost'
    start = order.startLocation
    finish = order.finishLocation
    cost = order.cost
    time = order.time
    total_cost = sum(ITEMS[i].cost for i in items)
    start_id = -1 if start is None else start
    reachable_nodes = None
    if start is None:
        start_name = '-'
    else:
        reachable_nodes = DELIVERY_SERVICE.getGraph().getReachableNodes(start_id)
        for node in nodes:
            if node.id == start_id:
                start_name = node.name
                break
    finish = '-' if finish is None else str(finish)
    route = '-' if route is None else str(route)
    items = '-' if items is None else str(items)
    cost = '-' if cost is None else str(cost * total_cost)
    time = '-' if time is None else str(time)
    context = {'order_id' : id, 'items' : items, 'start' : start_name, 'start_id': start_id,
                        'finish' : finish, 'route' : route, 'criteria' : criteria,
                        'cost' : cost, 'time' : time,
                        'pool' : str(ITEMS), 'reachable_nodes': reachable_nodes,
                        'nodes': nodes}
    return render(request, 'configure.html', context)

@shows_error
@require_POST
def add_item(request):
    order_id = int(request.POST['order_id'])
    item_id = int(request.POST['item_id'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.addItemToOrder(order_id, item_id)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@shows_error
@require_POST
def del_item(request):
    order_id = int(request.POST['order_id'])
    item_id = int(request.POST['item_id'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.deleteItemFromOrder(order_id, item_id)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@shows_error
@require_POST
def set_start_location(request):
    order_id = int(request.POST['order_id'])
    location = int(request.POST['location'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.setStartLocation(order_id, location)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@shows_error
@require_POST
def set_finish_location(request):
    order_id = int(request.POST['order_id'])
    location = int(request.POST['location'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.setFinishLocation(order_id, location)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@shows_error
@require_POST
def set_criteria(request):
    try:
        order_id = int(request.POST['order_id'])
        criteria = int(request.POST['criteria'])
        if criteria == 0:
            criteria = Criteria.time
        else:
            criteria = Criteria.cost
        global DELIVERY_SERVICE
        DELIVERY_SERVICE.setCriteria(order_id, criteria)
        return redirect(reverse(configure_order, kwargs={'id' : order_id}))
    except:
        return redirect(reverse(configure_order, kwargs={'id' : order_id}))


@require_POST
@shows_error
def build_route(request):
    order_id = int(request.POST['order_id'])
    global DELIVERY_SERVICE
    try:
        route_description = DELIVERY_SERVICE.buildRouteForOrder(order_id)
        print("ROUTE: ", route_description)
        G = nx.DiGraph()
        edge_labels = {}
        node_labels = {}
        for edge in route_description:
            G.add_edges_from([(edge[0],edge[1])], weight=1)
            edge_labels[(edge[0], edge[1])] = edge[2]
            node_labels[edge[0]] = edge[0]
        pos=nx.spring_layout(G)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
        nx.draw_networkx_labels(G,pos,node_labels,font_size=16)
        nx.draw(G,pos,node_size=1500,edge_color='black', node_color='blue')
        # plt.show()
        plt.savefig("delivery/static/img/" + str(order_id) + ".png", format="PNG")
        plt.close()
        G.clear()
    except:
        raise ObjectDoesNotExist('Cant build route')
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@shows_error
def lookup(request):
    check_user(request, 'users')
    global DELIVERY_SERVICE
    history = DELIVERY_SERVICE.getHistory()
    def format_history(entry):
        return '\n'.join(['Order:%s' % entry[0]] + 
                         [("Leg: %s Time: %s") % (e[1], datetime.datetime.fromtimestamp(e[0])) for e in entry[1]])
    hist_str = '\n\n'.join(map(format_history, history.items()))

    return render(request, 'lookup.html', {'history': hist_str})

@shows_error
def move(request):
    global DELIVERY_SERVICE
    check_user(request, 'couriers')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            try:
                order = DELIVERY_SERVICE.orders_dict[id]
            except:
                raise Http404("Order ID not found")    
            check_user(request, 'couriers', 'cour_' + str(order.getLocation().getId()))
            try:              
                print ('MOVE')
                print (DELIVERY_SERVICE.orders_dict)
                DELIVERY_SERVICE.moveOrder(id)
                print ('MOVED')
                return redirect(reverse(homepage))
                # return render(request, 'move.html', {'id' : id})
            except Exception as e:
                print (e)
                raise Http404("Order ID not found")    
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})

@shows_error
def fail(request):
    check_user(request, 'couriers')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            try:
                order = DELIVERY_SERVICE.orders_dict[id]
            except:
                raise Http404("Order ID not found")    
            check_user(request, 'couriers', 'cour_' + str(order.getLocation().getId()))
            try:
                global DELIVERY_SERVICE
                DELIVERY_SERVICE.reportFail(id, True)
                # return redirect(reverse(homepage))
                return render(request, 'report_fail.html', {'id' : id})
            except:
                raise Http404("Order ID not found")    
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})