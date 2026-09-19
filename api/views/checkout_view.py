from rest_framework.views import APIView
from rest_framework.response import Response


from store1.models import Products, Order, Customer

from rest_framework.permissions import IsAuthenticated
from api.authentication import CustomerJWTAuthentication

class CustomerCheckoutAPI(APIView):
    authentication_classes=[CustomerJWTAuthentication]
    permission_classes=[IsAuthenticated]

    def post(self, request):      

        customer_id = request.auth['customer_id']

        customer = Customer.objects.filter(id=customer_id).first()

        if not customer:
            return Response(   {'error': 'Customer not found'},   status=404       )

        cart = request.session.get('cart', {})

        if not cart:
            return Response(  {'error': 'Cart is empty'},  status=400    )

        address = request.data.get('address')
        city = request.data.get('city')
        state = request.data.get('state')
        pincode = request.data.get('pincode')
        phone = request.data.get('phone')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        if not address or not city or not state or not pincode or not phone:
            return Response(
                {'error': 'All delivery details are required'},
                status=400
            )

        products = Products.objects.filter(id__in=cart.keys())

        orders = []

        for product in products:

            quantity = cart.get(str(product.id), 0)

            if quantity <= 0:
                continue

            order = Order.objects.create(
                customer=customer,
                product=product,
                price=product.price,
                quantity=quantity,
                address=address,
                city=city,
                state=state,
                pincode=pincode,
                phone=phone,
                latitude=latitude,
                longitude=longitude
            )

            orders.append({
                'order_id': order.id,
                'product': product.name,
                'quantity': quantity,
                'price': product.price,
                'total_price': product.price * quantity
            })

        request.session['cart'] = {}
        request.session.modified = True

        return Response({
            'message': 'Order placed successfully',
            'orders': orders
        }, status=201)