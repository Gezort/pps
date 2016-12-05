from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^login(?P<next>.+)$', views.login, name='login'),
    url(r'^logout(?P<next>.+)$', views.logout, name='logout'),
    url(r'^register(?P<next>.+)$', views.register, name='register'),

]
