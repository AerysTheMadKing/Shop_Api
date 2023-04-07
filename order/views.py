from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from order import serializers
from order.models import Order


class OrderApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


    def get(self, request, *args, **kwargs):
        user = request.user
        orders = user.orders.all()
        serializer = serializers.OrderSerializer(instance=orders, many=True).data
        return Response(serializer, status=200)
