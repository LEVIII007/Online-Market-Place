from django.shortcuts import render, redirect
from items.models import Item, Category
from .forms import SignupForm, loginform



# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False).order_by('id')[:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        "items": items,
        "categories": categories
    })
def contact(request):
    return render(request, "core/contact.html")

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, "core/signup.html", {
        "form": form
    })


# def login(request):
#     form = loginform()
#     if request.method == 'POST':
#         form = SignupForm(request.POST)

#     if form.is_valid():
#         form.save()
#         return redirect('/items/')
#     else:
#         form = loginform()
#     return render(request, "core/login.html", {
#         "form": form
#     })