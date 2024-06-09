from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def index(request):
    return render(request, 'dashboard/index.html')
@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required
def product(request):
    items = Product.objects.all()   
    form = ProductForm()
    if request.method=='POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard-product")
    context={'items':items,'formproduct': form}
    return render(request, 'dashboard/product.html', context)

@login_required
def order(request):
    return render(request, 'dashboard/order.html')


# def addProduct(request):
#     form = ProductForm()
#     if request.method=='POST':
#         form= ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("dashboard-product")
#     context={'formproduct': form}
#     return render(request, 'dashboard/product.html', context)

@login_required
def delete(request, pk):
    context={'itemId': pk}
    return render(request, 'dashboard/delete-product.html', context)
@login_required
def deleteProduct(request, pk):
    item = Product.objects.get(id=pk)
    if item:
        item.delete()
        return redirect('dashboard-product')
    # context={'item': item}
    # return render(request, 'dashboard/delete-product.html', context)


@login_required
def editProduct(request, pk):
    item = Product.objects.get(id=pk)
    form = ProductForm(instance=item)
    if request.method =='POST':
        form = ProductForm(request.POST, instance=item)
        print('work here')
        if form.is_valid():
            print('not work here')
            form.save()
            return redirect("dashboard-product")
    context={'formedit':form}
    return render(request, 'dashboard/edit-product.html', context)