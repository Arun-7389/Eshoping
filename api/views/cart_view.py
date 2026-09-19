from rest_framework.views import APIView
from rest_framework.response import Response

from store1.models.Product import Products

from rest_framework.permissions import IsAuthenticated
from api.authentication import CustomerJWTAuthentication

class CustomerCartAPI(APIView):
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):

        cart= request.session.get('cart',{})

        ids=[int(i)  for i in cart.keys() if str(i).isdigit()]

        products =Products.objects.filter(id__in=ids)

        data=[]
        for product in products:
            quantity = cart.get(str(product.id),0)
            data.append({
                'id':product.id,
                'name':product.name,
                'price':product.price,
                'quantity':quantity,
                'total_price':product.price * quantity,
                     })
        return Response(data)
    
class CustomerCartAddAPI(APIView):
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):

        product_id =request.data.get('product_id')

        if not product_id:
            return Response({'error':'Product_id is required'},status=400)

        product =Products.objects.filter(id=product_id).first()

        if not product:
            return Response({'error':'Product Not Found'},status=404  )
        cart = request.session.get('cart',{})

        product_id=str(product_id)

        if product_id in cart:
            cart[product_id] += 1
        else:
            cart[product_id]=1

        request.session['cart']=cart
        request.session.modified =True
        return Response({'message':'Product Added to cart', 'cart':cart})

class CustomerCartRemoveAPI(APIView):
    authentication_classes = [CustomerJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):

        product_id=request.data.get('product_id')
        if not product_id:
            return Response({'error':'Product_id is required'},status=400)

        cart=request.session.get('cart',{})
        product_id=str(product_id)

        if product_id not in cart:
            return Response({'error':'Product is not in cart'},status=400)

        if cart[product_id] <=1:
            cart.pop(product_id)
        else:
            cart[product_id] -=1

        request.session['cart']=cart
        request.session.modified =True

        return Response({'message':'Product remove from cart', 'cart':cart})