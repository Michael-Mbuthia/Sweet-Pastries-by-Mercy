from django.urls import path
from .views import CheckoutView, OrderHistoryView

urlpatterns = [
    path("checkout/", CheckoutView.as_view()),
    path("", OrderHistoryView.as_view()),
]