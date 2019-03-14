from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin$', views.admin),
    url(r'^go_register$', views.go_register),
    url(r'^register$', views.register),
    url(r'^get_pant_info/(.+)/$', views.get_pant_info),
    url(r'^check_lower/(?P<upper_id>\d+)$', views.check_lower),
    url(r'^product_detail/(?P<product_id>\d+)$', views.product_detail),
    url(r'^get_upper_product/(?P<upper_id>\d+)$', views.get_upper_product),
    url(r'^go_cart/(?P<product_id>\d+)$', views.go_cart),
]