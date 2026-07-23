from django import template

register=template.Library()

@register.filter(name='get_item')
def get_item(dictionary,key):
    return dictionary.get(str(key))

@register.filter(name='cart_total')
def cart_total(product,cart):
    quantity=cart.get(str(product.id))
    return product.price* quantity

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    return str(product.id)in cart
