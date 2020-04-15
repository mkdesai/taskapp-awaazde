from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='addclass')
def addclass(field, class_attr):
    return field.as_widget(attrs={'class': class_attr})
