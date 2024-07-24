from django.urls import path, include
from portfolio.views import home

urlpatterns = [
    path("home/", home, name="home")
    ]
