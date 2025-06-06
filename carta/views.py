from django.shortcuts import render
from .models import Item

# Create your views here.

def index(request):
    items = Item.objects.filter(stock__gt=0)
    #items = Item.objects.all()
    context = {
        'items': items,
        }
    return render(request, 'carta/carta.html', context)
