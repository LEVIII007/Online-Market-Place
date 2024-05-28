from django.shortcuts import render
from items.models import Item, Category



# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False).order_by[0:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        "items": items,
        "categories": categories
    })
def contact(request):
    return render(request, "core/contact.html")