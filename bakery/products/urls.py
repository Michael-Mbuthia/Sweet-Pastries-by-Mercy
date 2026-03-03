from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path("", ProductListView.as_view()),
    path("<int:pk>/", ProductDetailView.as_view()),
    path("create/", ProductCreateView.as_view()),
    path("<int:pk>/update/", ProductUpdateView.as_view()),
    path("<int:pk>/delete/", ProductDeleteView.as_view()),
]
