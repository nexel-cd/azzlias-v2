
from django.urls import path
from .views import *


urlpatterns = [

    path('',home,name="home"),
    path('category',category,name="category"),
    path('contactus',contactus,name="contactus"),
    path('shop/', shop, name='shop'),
    path('shop/<pk>', shop_details, name='shop_details'),
    path('shopbycategory/<cat>', shop_category, name='shop_category'),

]
