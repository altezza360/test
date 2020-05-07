from django.shortcuts import render, redirect, HttpResponse
from .models import Specialist, Product, Order, Customer
from .forms import SpecialistForm, OrderForm, CustomerForm, RegisterForm
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import check, allowed_users
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/login/')
@check
def base(request):
    orders = Order.objects.all()
    total_order = Order.objects.count()
    pending_orders = Order.status
    products = Product.objects.all()
    specialists = Specialist.objects.all()
    context = {'orders': orders, 'products': products,
               'specialists': specialists, 'total_order': total_order,
               'pending_orders': pending_orders}
    return render(request, 'accounts/test.html', context)

@login_required(login_url='/login/')
@check
def manager(request):
    orders = Order.objects.all()
    total_orders = Order.objects.count()
    delivered_p = list(Order.objects.filter(status='delivered').aggregate(Sum('price')).values())[0]
    pending_p = list(Order.objects.filter(status='pending').aggregate(Sum('price')).values())[0]
    in_process_p = list(Order.objects.filter(status='order in process').aggregate(Sum('price')).values())[0]
    pending = Order.objects.filter(status='pending').count()
    in_process = Order.objects.filter(status='order in process').count()
    delivered = Order.objects.filter(status='delivered').count()
    specialists = Specialist.objects.all()
    context = {'orders': orders, 'total_orders': total_orders,  'pending': pending,
               'in_process': in_process, 'delivered': delivered, 'specialists': specialists,
               'delivered_p': delivered_p, 'pending_p': pending_p, 'in_process_p': in_process_p}
    return render(request, 'accounts/manager_page.html', context)


@login_required(login_url='/login/')
@check
def specialist_view(request, pk):
    specialist = Specialist.objects.get(id=pk)
    pending = specialist.order_set.filter(status='pending').count()
    in_process = specialist.order_set.filter(status='order in process').count()
    delivered = specialist.order_set.filter(status='delivered').count()

    total_orders = pending + in_process + delivered
    delivered_p= list(specialist.order_set.filter(status='delivered').aggregate(Sum('price')).values())[0]
    pending_p = list(specialist.order_set.filter(status='pending').aggregate(Sum('price')).values())[0]
    in_process_p = list(specialist.order_set.filter(status='order in process').aggregate(Sum('price')).values())[0]
    context = {'specialist': specialist, 'pending': pending, 'in_process': in_process,
              'delivered': delivered, 'total_orders': total_orders, 'delivered_p': delivered_p,
               'pending_p': pending_p, 'in_process_p': in_process_p}
    return render(request, 'accounts/specialist_view.html', context)

@login_required(login_url='/login/')
@check
def create_specialist(request):
    if request.method == 'POST':
        form = SpecialistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manager_page/')
    form = SpecialistForm()
    context = {'form': form}
    return render(request, 'accounts/create_specialist.html', context)



@login_required(login_url='/login/')
@check
def create_order(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        form2 = OrderForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('/manager_page/')
    else:
        form = CustomerForm()
        form2 = OrderForm()
    context = {'form': form, 'form2': form2}
    return render(request, 'accounts/create_order.html', context)

@login_required(login_url='/login/')
@check
def edit_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/manager_page/')
    else:
        form = OrderForm(instance=order)
    context = {'form': form, 'order': order}
    return render(request, 'accounts/edit_order.html', context)


@login_required(login_url='/login/')
@check
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/manager_page/')
    context = {'order': order}
    return render(request, 'accounts/delete_order.html', context)


@login_required(login_url='/login/')
@check
def customers(request):
    customers = Customer.objects.all()
    # order = customers.order.description.all()
    context = {'customers': customers}
    return render(request, 'accounts/customers.html', context)


@login_required(login_url='/login/')
@check
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required(login_url='/login/')
@allowed_users('specialist')
def user_page(request):
    try:
        orders = request.user.specialist.order_set.all()
        pending = orders.filter(status='pending').count()
        in_process = orders.filter(status='order in process').count()
        delivered = orders.filter(status='delivered').count()
        total_orders = pending + in_process + delivered
        delivered_p = list(orders.filter(status='delivered').aggregate(Sum('price')).values())[0]
        pending_p = list(orders.filter(status='pending').aggregate(Sum('price')).values())[0]
        in_process_p = list(orders.filter(status='order in process').aggregate(Sum('price')).values())[0]
    except ObjectDoesNotExist:
        return HttpResponse('I think User dont have a specialist')
    context = {'orders': orders, 'pending': pending, 'in_process': in_process, 'delivered': delivered,
               'total_orders': total_orders, 'delivered_p': delivered_p, 'pending_p': pending_p, 'in_process_p': in_process_p}
    return render(request, 'accounts/user_page.html', context)

# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password =request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('base_url')
#         else:
#             messages.info(request, 'Username OR password is incorrect')
#     context = {}
#     return render(request, 'accounts/login.html', context)
#
#
# def logoutUser(request):
#     logout(request)
#     return redirect('login')


