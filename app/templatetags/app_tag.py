from ..models import Name_Cinema
from django import template

register = template.Library()

@register.simple_tag()
def cinema_tag():
    name = Name_Cinema.objects.all()[0]
    return name