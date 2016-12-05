from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.http import Http404, HttpResponseRedirect
from .forms import OrderIdForm
from .logic.delivery_service import DeliveryService
from .logic.graph import Graph
 
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
            id = form.cleaned_data['id']
            try:
                global DELIVERY_SERVICE
                DELIVERY_SERVICE.deleteOrder(id)    
                return render(request, 'delete_order.html', {'id' : id})
            except:
                raise Http404("Order ID not found")    
        else:
            raise Http404("Order ID not found")
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def launch(request):
    check_user(request, 'users')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            try:
                global DELIVERY_SERVICE
                launched = DELIVERY_SERVICE.launchOrder(id)
                return render(request, 'launch_order.html', {'launched' : launched})
            except:
                raise Http404("Order does not exist or not configured") 
        else:
            raise Http404("Order ID not found")
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def track(request):
    check_user(request, 'users')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            try:
                # global DELIVERY_SERVICE
                # DELIVERY_SERVICE.deleteOrder(id)
                # ?????????????    
                return render(request, 'track_order.html', {'id' : id})
            except:
                raise Http404("Order ID not found")    
        else:
            raise Http404("Order ID not found")
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def configure(request):
    check_user(request, 'users')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            try:
                # global DELIVERY_SERVICE
                # DELIVERY_SERVICE.deleteOrder(id)
                # ?????????????    
                return render(request, 'configure_order.html', {'id' : id})
            except:
                raise Http404("Order ID not found")    
        else:
            raise Http404("Order ID not found")
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def lookup(request):
    check_user(request, 'users')
    return render(request, 'lookup.html')


def move(request):
    check_user(request, 'couriers')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            try:
                # global DELIVERY_SERVICE
                # DELIVERY_SERVICE.deleteOrder(id)
                # ?????????????    
                return render(request, 'move.html', {'id' : id})
            except:
                raise Http404("Order ID not found")    
        else:
            raise Http404("Order ID not found")
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})


def fail(request):
    check_user(request, 'users')
    if request.method == 'POST':
        form = OrderIdForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            try:
                # global DELIVERY_SERVICE
                # DELIVERY_SERVICE.deleteOrder(id)
                # ?????????????    
                return render(request, 'report_fail.html', {'id' : id})
            except:
                raise Http404("Order ID not found")    
        else:
            raise Http404("Order ID not found")
    else:
        form = OrderIdForm()
    return render(request, 'input_order_id.html', {'form' : form})