from django.shortcuts import render, get_object_or_404

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(item, pk=pk)
    related_items = item.object.filter(category=item.category, is_sold = False).exclude(pk=item.pk)
    return render(request, "items/detail.html",{
        'item': item
    })

