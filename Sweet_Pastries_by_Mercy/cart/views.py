from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Cart, CartItem
from .serializers import CartSerializer
from products.models import Product


def get_user_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart


class ViewCart(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = get_user_cart(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product")
        quantity = int(request.data.get("quantity", 1))

        product = get_object_or_404(Product, id=product_id)

        if quantity > product.stock_quantity:
            return Response(
                {"error": "Not enough stock available"},
                status=400
            )

        cart = get_user_cart(request.user)
        item, created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )

        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity

        if item.quantity > product.stock_quantity:
            return Response(
                {"error": "Quantity exceeds stock"},
                status=400
            )

        item.save()
        return Response({"message": "Added to cart"})


class UpdateCartItem(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        item_id = request.data.get("item_id")
        quantity = int(request.data.get("quantity"))

        cart = get_user_cart(request.user)
        item = get_object_or_404(CartItem, id=item_id, cart=cart)

        if quantity > item.product.stock_quantity:
            return Response(
                {"error": "Not enough stock"},
                status=400
            )

        item.quantity = quantity
        item.save()

        return Response({"message": "Cart updated"})


class RemoveCartItem(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        item_id = request.data.get("item_id")

        cart = get_user_cart(request.user)
        item = get_object_or_404(CartItem, id=item_id, cart=cart)
        item.delete()

        return Response({"message": "Item removed"})