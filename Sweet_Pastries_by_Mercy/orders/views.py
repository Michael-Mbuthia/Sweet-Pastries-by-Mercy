from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({"error": "Cart empty"}, status=400)

        items = cart.items.all()
        if not items:
            return Response({"error": "Cart empty"}, status=400)

        total = 0

        # stock validation
        for item in items:
            if item.quantity > item.product.stock_quantity:
                return Response(
                    {"error": f"Not enough stock for {item.product.name}"},
                    status=400
                )
            total += item.quantity * item.product.price

        order = Order.objects.create(
            user=request.user,
            total_price=total
        )

        # create order items + deduct stock
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price_at_purchase=item.product.price
            )

            item.product.stock_quantity -= item.quantity
            item.product.save()

        cart.items.all().delete()

        return Response({"message": "Order placed"})


class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by("-created_at")
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)