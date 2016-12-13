from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_GET, require_POST
from django.http import Http404, HttpResponseRedirect
from .forms import OrderIdForm, ConfigureOrderForm
from .logic.delivery_service import DeliveryService
from .logic.graph import Graph
from .logic.item import Item
from .logic.order import Criteria
from .logic.list_items import ITEMS 

DELIVERY_SERVICE = DeliveryService(Graph())


def check_user(request, group):
    user = request.user
    if  user is None or (not user.is_authenticated()) or str(user.groups.all()[0]) != group:
        raise Http404("You can't access this page")


@require_GET
def index(request):
    return render(request, 'index.html')


@require_GET
def homepage(request):
    user = request.user
    if  user is None or (not user.is_authenticated()):
        raise Http404("You aren't authenticated")
    context={'is_courier' : str(request.user.groups.all()[0]) == 'couriers'}
    return render(request, 'homepage.html', context=context)


@require_GET
def create(request):
    check_user(request, 'users')
    global DELIVERY_SERVICE
    order_id = DELIVERY_SERVICE.addOrder()
    return render(request, 'create_order.html', {'id' : order_id})


def delete(request):
    check_user(request, 'users')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            try:
                global DELIVERY_SERVICE
                DELIVERY_SERVICE.deleteOrder(id)    
                return render(request, 'delete_order.html', {'id' : id})
            except:
                raise Http404("Order ID not found")    
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def launch(request):
    check_user(request, 'users')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            try:
                global DELIVERY_SERVICE
                launched = DELIVERY_SERVICE.launchOrder(id)
                return render(request, 'launch_order.html', {'launched' : launched})
            except:
                raise Http404("Order does not exist or not configured") 
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


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
                    raise
                return render(request, 'track_order.html', {'location' : location})
            except:
                raise Http404("Order ID not found")    
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def configure(request):
    check_user(request, 'users')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            return redirect(reverse(configure_order, kwargs={'id' : id}))
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def configure_order(request, id):
    check_user(request, 'users')
    global DELIVERY_SERVICE
    global ITEMS
    if int(id) not in DELIVERY_SERVICE.orders_dict:
        raise Http404("Order ID not found")

    order = DELIVERY_SERVICE.orders_dict[int(id)]
    items = order.itemList
    route = order.route
    criteria = 'time' if order.criteria == Criteria.time else 'cost'
    start = order.startLocation
    finish = order.finishLocation
    
    start = '-' if start is None else str(start)
    finish = '-' if finish is None else str(finish)
    route = '-' if route is None else str(route)
    items = '-' if items is None else str(items)
    context = {'order_id' : id, 'items' : items, 'start' : start, 
                        'finish' : finish, 'route' : route, 'criteria' : criteria,
                        'pool' : str(ITEMS)}
    return render(request, 'configure.html', context)

@require_POST
def add_item(request):
    order_id = int(request.POST['order_id'])
    item_id = int(request.POST['item_id'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.addItemToOrder(order_id, item_id)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@require_POST
def del_item(request):
    order_id = int(request.POST['order_id'])
    item_id = int(request.POST['item_id'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.deleteItemFromOrder(order_id, item_id)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@require_POST
def set_start_location(request):
    order_id = int(request.POST['order_id'])
    location = int(request.POST['location'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.setStartLocation(order_id, location)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@require_POST
def set_finish_location(request):
    order_id = int(request.POST['order_id'])
    location = int(request.POST['location'])
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.setFinishLocation(order_id, location)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@require_POST
def set_criteria(request):
    order_id = int(request.POST['order_id'])
    criteria = int(request.POST['criteria'])
    if criteria == 0:
        criteria = Criteria.time
    else:
        criteria = Criteria.cost
    global DELIVERY_SERVICE
    DELIVERY_SERVICE.setCriteria(order_id, criteria)
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

@require_POST
def build_route(request):
    order_id = int(request.POST['order_id'])
    global DELIVERY_SERVICE
    try:
        DELIVERY_SERVICE.buildRouteForOrder(order_id)
    except:
        Http404('Cant build route')
    return redirect(reverse(configure_order, kwargs={'id' : order_id}))

def lookup(request):
    check_user(request, 'users')
    return render(request, 'lookup.html')


def move(request):
    check_user(request, 'couriers')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            try:
                global DELIVERY_SERVICE
                print ('MOVE')
                print (DELIVERY_SERVICE.orders_dict)
                DELIVERY_SERVICE.moveOrder(id)
                return render(request, 'move.html', {'id' : id})
            except Exception as e:
                print (e)
                raise Http404("Order ID not found")    
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def fail(request):
    check_user(request, 'couriers')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = int(form.cleaned_data['id'])
            try:
                global DELIVERY_SERVICE
                DELIVERY_SERVICE.reportFail(id)
                return render(request, 'report_fail.html', {'id' : id})
            except:
                raise Http404("Order ID not found")    
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})