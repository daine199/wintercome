
# Owner Daine.H
# Modify 2016-01-05

from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^cmdindex/$', views.cmd_index_page, name='cmd-index-page'),
    url(r'^basiccall/(?P<cmd_id>[0-9]+)/$', views.basic_cmd_run, name='basic-cmd-call'),
    url(r'^sign/$', views.sign_up_page, name='sign-page'),
    url(r'^index/$', views.index_page, name='index'),
    url(r'^logout/$', views.logout_page, name='logout-page'),
    # url(r'^userlist/$',
    #     views.user_list_page,
    #     name='user-list')
]