from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from store1.models.Customer import Customer

class CustomerJWTAuthentication(JWTAuthentication):

    def get_user(self, validated_token):

        customer_id = validated_token.get('customer_id')

        if not customer_id:
             raise InvalidToken('Token contained no customer identification')

        customer = Customer.objects.filter(id=customer_id).first()

        if not customer:
            raise InvalidToken('Customer not found')
        customer.is_authenticated = True

        return customer