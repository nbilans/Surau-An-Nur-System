from django.urls import path
from . import views
from .views import create_order, order_detail


urlpatterns=[
    path("",views.home,name="home"),
    path("profile_list/",views.profile_list,name="profile_list"),
    path("profile/<int:pk>",views.profile,name="profile"),

    path("login/",views.login_user,name="login"),
    path("logout/",views.logout_user,name="logout"),

    path("register/",views.register_user,name="register"),
    path("register_emp/",views.register_employee,name="register_emp"),

    path("item/",views.customer_item,name="customer_item"),
    path("vieworder/",views.view_order,name="view_order"),
    path("deleteorder/<str:Itemid>",views.deleteorder,name="deleteorder"),
    path("updateorder/<str:Itemid>",views.update_item,name="update_item"),
    path("updateorder/update_data/<str:Itemid>",views.update_data, name="update_data"),

    path("viewcustomer/",views.view_customer,name="view_customer"),
    path("deletecustomer/<str:Userid>",views.deletecustomer,name="deletecustomer"),
    path("updatecustomer/<str:Userid>",views.update_customer,name="update_customer"),
    path("updatecustomer/update_datacustomer/<str:Userid>",views.update_datacustomer, name="update_datacustomer"),

    path("viewemployee/",views.view_employee,name="view_employee"),
    path("deleteemployee/<str:Employeeid>",views.deleteemployee,name="deleteemployee"),
    path("updateemployee/<str:Employeeid>",views.update_employee,name="update_employee"),
    path("updateemployee/update_dataemployee/<str:Employeeid>",views.update_dataemployee, name="update_dataemployee"),

    path('searchpage',views.searchpage,name="searchpage"),
    path('searchorder/', views.search_order, name='search_order'),

    path('orders/create/', create_order, name='create_order'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/', views.order_list, name='order_list'),

    path('order_detail/<int:pk>/', views.order_detail, name='booking_detail'),
    path('order_list/<int:pk>/', views.order_detail, name='booking_detail'),
]