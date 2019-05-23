from django.conf.urls import url
from . import views

app_name = 'barang'

urlpatterns = [
    url(r'^$',views.data_barang),
    url(r'^e_order/(?P<pk>\d+)/$',views.edit_barang),
    url(r'^new/$',views.new_order),
    ]
