from django.urls import path
from . import views

app_name= 'portfolios'

urlpatterns =[
    path("", views.index, name="index"),
    path("danhmuc", views.my_portfolio, name="my_portfolio"),
    path("buy", views.buy, name="buy"),
    path("sell", views.sell, name="sell"),
    path("history", views.history, name="history")
    

]