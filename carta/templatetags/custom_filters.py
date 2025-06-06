from django import template

register = template.Library()

@register.filter
def pesos_cl(n):
    return f'${n:,d}'.replace(',','.')
