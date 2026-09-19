from rest_framework.views import APIView
from rest_framework.response import Response

from store1.models.orders import Order
from api.serializers.order_serializers import OrderSerializer

from rest_framework.permissions import IsAuthenticated
from api.authentication import CustomerJWTAuthentication
from api.pagination import MyStorePagination


class CustomerOrderListAPI(APIView):
        authentication_classes =[CustomerJWTAuthentication]
        permission_classes =[IsAuthenticated]

        def get(self,request):
                customer_id = request.auth['customer_id']

                orders=Order.objects.filter(customer_id=customer_id).order_by('-date')

                paginator = MyStorePagination()
                page =paginator.paginate_queryset(orders,request)

                serializer = OrderSerializer(page,many=True)

                return paginator.get_paginated_response(serializer.data)
        
class CustomerOrderDetailAPI(APIView):

        authentication_classes =[CustomerJWTAuthentication]
        permission_classes =[IsAuthenticated]

        def get(self,request,order_id):

                customer_id = request.auth['customer_id']
        
                order=Order.objects.filter(id=order_id,customer_id=customer_id).first()

                if not order:
                        return Response({'error':'Oder Not Found'},status=404)

                serializer=OrderSerializer(order)

                return Response(serializer.data)
                        
        
        
