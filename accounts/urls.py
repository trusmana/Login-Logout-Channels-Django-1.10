from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth

app_name = 'accounts'

urlpatterns =[
    url(r'^login/$', views.login_views, name="login"),
    url(r'^logout/$', auth.logout, {'next_page': '/'}, name='logout'),
    url(r'^change_password/$', login_required(auth.password_change),\
       {'post_change_redirect' : '/','template_name': 'registration/change_password.html'}, name='change_password'),
]
