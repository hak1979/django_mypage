''' urls.py to register the urls of the different pages for the personal app'''

# import libraries
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('details/', views.details, name="details"),
    path('shop/', views.shop, name="shop")
]
