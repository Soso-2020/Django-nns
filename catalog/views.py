from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from .models import Item
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from cart.forms import CartAddProductForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Register successfully")
            return redirect('index')
        else:
            messages.error(request, "Error")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form': form})



@login_required
def index(request):
    item_name = Item.objects.all()
    item_cost = Item.objects.all()
    item_descr = Item.objects.all()
    item_image = Item.objects.all()
    context = {
        'item_name': item_name,
        'item_cost': item_cost,
        'item_descr': item_descr,
        'item_image': item_image,
    }
    return render(request, "index.html", context=context)


class item_call(DetailView):
    model = Item
    template_name = 'item.html'
    obj_name = 'item'

    def item(request):
        item_name = Item.objects.all()
        item_cost = Item.objects.all()
        item_descr = Item.objects.all()
        item_image = Item.objects.all()
        context = {
            'item_name': item_name,
            'item_cost': item_cost,
            'item_descr': item_descr,
            'item_image': item_image,
        }
        return render(request, "item.html", context=context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def logon(request):
    return render(request, "registration/login.html")


def product_detail(request, id, slug):
    product = get_object_or_404(Item,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'cart/templates/cart/detail.html', {'product': product, 'cart_product_form': cart_product_form})

# Create your views here.
