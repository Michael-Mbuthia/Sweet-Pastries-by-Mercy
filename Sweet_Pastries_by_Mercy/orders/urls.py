from django.urls import path
from .views import CheckoutView, OrderHistoryView
from .views_admin import AdminOrderListView, AdminOrderUpdateView

urlpatterns = [
    path("checkout/", CheckoutView.as_view()),
    path("", OrderHistoryView.as_view()),
    path("admin/", AdminOrderListView.as_view()),
    path("admin/<int:pk>/", AdminOrderUpdateView.as_view()),
]