from django.urls import path
from .views import ViewCart, AddToCart, UpdateCartItem, RemoveCartItem

urlpatterns = [
    path("", ViewCart.as_view()),
    path("add/", AddToCart.as_view()),
    path("update/", UpdateCartItem.as_view()),
    path("remove/", RemoveCartItem.as_view()),
]