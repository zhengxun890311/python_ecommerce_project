from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^admin$', views.index),
    url(r'^createNewProduct$', views.createNewProduct),
    url(r'^admin_register$', views.admin_register),
    url(r'^admin_login$', views.admin_login),
    url(r'^admin_first_page$', views.admin_first_page),
    url(r'^admin_register_page$', views.admin_register_page),
    url(r'^admin_category_management$', views.admin_category_management),
    url(r'^delete_admin/(?P<admin_id>\d+)$', views.delete_admin),
    url(r'^createNewLowerCategory$', views.createNewLowerCategory),
    url(r'^delete_Product/(?P<product_id>\d+)$', views.delete_Product),

    url(r'^show_product/(?P<product_id>\d+)$', views.show_product),
        
    url(r'^product_info$', views.product_info),
    url(r'^log_out$', views.log_out),
    url(r'^delte_Category/(?P<category_id>\d+)$', views.delte_Category),
    url(r'^get_lower_category$', views.get_lower_category),
    url(r'^user_management$', views.user_management),
    url(r'^user_register$', views.user_register),
    url(r'^delete_User/(?P<user_id>\d+)$', views.delete_User),
]