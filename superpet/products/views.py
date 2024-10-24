from django.shortcuts import render
from .models import Products,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

def products(request):
    return render(request,"products.html")


def royalCanin(request):
    products=Products.customManager.royalCanin()
    return render(request,"products.html",{"products":products})

def drools(request):
    products=Products.customManager.drools()
    return render(request,"products.html",{"products":products})


def search(request):
    keyword=request.GET.get("keyword")
    products=Products.customManager.all().filter(product_name__icontains=keyword)
    return render(request,"products.html",{"products":products})

class ProductListView(ListView):
    model=Products
    
class ProductDetailView(DetailView):
    model=Products
    template_name="products/productdetails.html"
    
class ProductCreateView(CreateView):
    model=Products
    fields="__all__"
    success_url="/products"
    
class ProductUpdateView(UpdateView):
    model=Products
    fields="__all__"
    success_url="/products"
    
class ProductDeleteView(DeleteView):
    model=Products
    success_url="/products"
    
class CategoryDetailView(DetailView):
    model=Category
    template_name="category/categorydetail.html"
    slug_field="category_slug"
    context_object_name="category_obj"