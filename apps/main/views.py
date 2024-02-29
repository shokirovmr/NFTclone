from django.views import View
from django.shortcuts import render

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