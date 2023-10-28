from products.views import *
from django.urls import path

urlpatterns = [
    # path('index/', index),
    # path('person/', person),
    # path('login/', login),
    path('products/', ProductAPI.as_view())
]
