"""canteenproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from canteenapp.views import *
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    ######## LOGIN & REGISTER START ###########
   
    url(r'^$',display_login),
    url(r'^Display_login',Display_login, name="Display_login"),
    url(r'^reg', reg, name="reg"),
    url(r'^user_reg', user_reg, name="user_reg"),
    url(r'^home_user',home_user, name="home_user"),
    url(r'^admin_home',admin_home, name="admin_home"),
    url(r'^check_login', check_login, name="check_login"),
    url(r'^showuser',showuser, name="showuser"),
    url(r'^Show_user',Show_user, name="Show_user"),
    url(r'^add_food_item',add_food_item, name="add_food_item"),
    url(r'^store_food_item',store_food_item, name="store_food_item"),
    url(r'^view_food',view_food, name="view_food"),
    url(r'^food_item',food_item, name="food_item"),
    url(r'^day_food',day_food, name="day_food"),
    url(r'^deleteevent',deleteevent, name="deleteevent"),
    url(r'^Day_food_view',Day_food_view, name="Day_food_view"),
    url(r'^Food_view_user',Food_view_user, name="Food_view_user"),
    url(r'^View_daily_item_page',View_daily_item_page, name="View_daily_item_page"),
    url(r'^order_food',order_food, name="order_food"),
    url(r'^Cart',Cart, name="Cart"),
    url(r'^cart_view',cart_view, name="cart_view"),
    url(r'^food_view_user',food_view_user, name="food_view_user"),
    url(r'^Aday_food_view',Aday_food_view, name="Aday_food_view"),
    url(r'^bill',bill, name="bill"),
    url(r'^View_bill',View_bill, name="View_bill"),
    url(r'^pay',pay, name="pay"),
    url(r'^cancel',cancel, name="cancel"),
    url(r'^logout',logout, name="logout"),
    url(r'^delete',delete, name="delete"),
    url(r'^Bill_view',Bill_view, name="Bill_view"),
    # url(r'^bill_view',bill_view, name="bill_view"),
    url(r'^Delete_bill',Delete_bill, name="Delete_bill"),
    url(r'^Remove_bill',Remove_bill, name="Remove_bill"),
    url(r'^User_bill',User_bill, name="User_bill"),
    url(r'^show_order_admin',show_order_admin, name="show_order_admin"),
    url(r'^Order_admin_view',Order_admin_view, name="Order_admin_view"),
    url(r'^edit_food',edit_food, name="edit_food"),
    url(r'^stats_view',stats_view, name="stats_view"),
    url(r'^statistics',statistics, name="statistics"),
    url(r'^search_date',search_date, name="search_date"),
    url(r'^decrement',decrement, name="decrement"),
    url(r'^increment',increment, name="increment"),
    url(r'^Increment_menu',Increment_menu, name="Decrement_menu"),
    url(r'^Decrement_menu',Decrement_menu, name="Decrement_menu"),
    url(r'^Delete_menu',Delete_menu, name="Delete_menu"),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    ##
]
