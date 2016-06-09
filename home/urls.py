from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^index/$', views.index, name='homepage'),
]