from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect

from apps.main.forms import ProductCreateForm
from apps.main.models import Product


# Create your views here.
def index(request):
    return render(request, 'users/../../templates/index.html')


def author(request):
    return render(request, 'main/author.html')


def create(request):
    return render(request, 'main/create.html')


def details(request):
    return render(request, 'main/details.html')


def explore(request):
    return render(request, 'main/explore.html')

class ProductLikeView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)

@login_required()
def post_create(request):
    if request.method == "POST":
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            item = Product(title=form.cleaned_data["title"], description=form.cleaned_data["description"],
                        category=form.cleaned_data["category"], ends_in=form.cleaned_data["ends_in"],
                        price=form.cleaned_data["price"],owner=form.cleaned_data["owner"],
                        image=form.cleaned_data["image"],
                        author=request.user)
            # item.author = request.user
            item.save()
            messages.success(request, "item successfully created")
            return redirect(reverse('main:author', kwargs={"username": request.user.username}))
        else:
            return render(request, "main/create.html", {"form": form})
    else:
        form = ProductCreateForm()
        return render(request, "main/create.html", {"form": form})