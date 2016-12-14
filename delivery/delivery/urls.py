from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.homepage, name='homepage'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/', views.delete, name='delete'),

    url(r'^configure/$', views.configure, name='configure'),
    url(r'^configure/(?P<id>[0-9]+)$', views.configure_order, name='configure_order'),
    url(r'^configure/set_start/$', views.set_start_location, name='set_start'),
    url(r'^configure/set_finish/$', views.set_finish_location, name='set_finish'),
    url(r'^configure/set_criteria/$', views.set_criteria, name='set_criteria'),
    url(r'^configure/add_item/$', views.add_item, name='add_item'),
    url(r'^configure/delete_item/$', views.del_item, name='delete_item'),
    url(r'^configure/build_route/$', views.build_route, name='build_route'),

    url(r'^launch/$', views.launch, name='launch'),
    url(r'^track/$', views.track, name='track'),
    url(r'^lookup/$', views.lookup, name='lookup'),
    
    url(r'^fail/$', views.fail, name='fail'),
    url(r'^move/$', views.move, name='move'),
]
