from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.homepage, name='homepage'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^configure/$', views.configure, name='configure'),
    url(r'^configure/(?P<id>[0-9]+)$', views.configure_order, name='configure_order'),
    url(r'^launch/$', views.launch, name='launch'),
    url(r'^track/$', views.track, name='track'),
    url(r'^lookup/$', views.lookup, name='lookup'),
    
    url(r'^fail/$', views.fail, name='fail'),
    url(r'^move/$', views.move, name='move'),
]
