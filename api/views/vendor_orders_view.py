from rest_framework.views import APIView
from rest_framework.response import Response

from store1.models.orders import Order
from api.serializers.order_serializers import OrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from api.pagination import MyStorePagination

class VendorOrderListAPI(APIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        vendor_id=request.auth['vendor_id']

        orders= Order.objects.filter(product__vendor_id=vendor_id).order_by('-date')

        paginator = MyStorePagination()
        page=paginator.paginate_queryset(orders,request)


        serializer=OrderSerializer(page,many=True)
        
        return paginator.get_paginated_response(serializer.data)
