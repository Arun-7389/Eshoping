from drf_spectacular.extensions import OpenApiAuthenticationExtension

class CustomerJWTAuthenticationschema(OpenApiAuthenticationExtension):
    target_class='api.authentication.CustomerJWTAuthentication'
    name='CutomerJWT'
    def get_security_definition(self, auto_schema):
        return {
            'type':'http',
            'schema':'bearer',
            'bearerFormat':'JWT'
        }