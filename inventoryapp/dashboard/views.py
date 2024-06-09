from django.shortcuts import render,redirect
from django.db.models import Count , Sum
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm

def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def index(request):
    orders= Order.objects.all()
    form = OrderForm()
    if request.method =='POST':
        form= OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.staff= request.user
            product_id = request.POST.get('product')
            product = Product.objects.get(id = product_id)
            if check_quantity(product, order):
                order.category= product.category
                product.quantity -= order.order_quantity
                order.save()
                product.save()
                print(product.quantity)
                return redirect('dashboard-index')
            else:
                form= OrderForm()
    context= {'orders': orders,'formorder': form,'value_by_product': value_by_product()[1], 'product_list': value_by_product()[0],'value_by_category': value_by_category()[1], 'category_list': value_by_category()[0]}
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    return render(request, 'dashboard/staff.html')

# @login_required
# def staffIndex(request):
    
#     return render(request, 'dashboard/staff-index.html', context)


@login_required
def staff(request):
    staffs = User.objects.all()
    context={
        'staffs': staffs
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    staff = User.objects.get(id= pk)
    context={'staff': staff}
    return render(request, 'dashboard/staff-detail.html', context)

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
    orders= Order.objects.all()
    context={
        'orders': orders
    }
    return render(request, 'dashboard/order.html', context)


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



def check_quantity(product, order):
    return product.quantity >= order.order_quantity


def value_by_category():
    
    category_count = Order.objects.values('product__category').annotate(total= Sum('order_quantity'))
    print(category_count)
    category= [obj['product__category'] for obj in category_count ]
    
    total = [obj['total'] for obj in category_count ]
    print(category, total)
    return [category, total]



def value_by_product():
    
    product_count = Order.objects.values('product__name').annotate(total= Sum('order_quantity'))
    product= [obj['product__name'] for obj in product_count ]
    
    total = [obj['total'] for obj in product_count ]
    print(product, total)
    return [product, total]


value_by_product()