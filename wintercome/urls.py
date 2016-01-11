
# Owner Daine.H
# Modify 2016-01-05

from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^cmdindex/$', views.cmd_index_page,
        name='cmd_index_page'),
    url(r'^basiccall/(?P<cmd_id>[0-9]+)/$',
        views.basic_cmd_run,
        name='basic-cmd-call'),
    url(r'^sign/$',
        views.sign_up_page,
        name='sign-page'),
    # url(r'^login/$',
    #     views.login_page,
    #     name='login-page'),
    # url(r'^userlist/$',
    #     views.user_list_page,
    #     name='user-list')
]