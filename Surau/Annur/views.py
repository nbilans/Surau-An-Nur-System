from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect;
from Annur.models import CusUsers,Item,Employee,Booking;
from django.db.models import Q;
from django.urls import reverse;
from django.contrib import messages
from .models import CusUsers, Item, Employee, Booking
from .forms import SignUpForm, EmpSignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db import models


#-----------------------------------------------------------------

#Home

def home(request):
    return render(request, 'home.html')

#-----------------------------------------------------------------

#Profile list/Profile

#view/GET

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        return render(request, "profile.html", {"profile":profile})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')

#-----------------------------------------------------------------

#Login and Logout Customer/Employee

#view/GET

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Successfully Logged In!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in. Please Try Again..."))
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Logged Out..."))
    return redirect('home')

#-----------------------------------------------------------------

#Register Customer

#Save data/POST

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            Userid = form.cleaned_data['Userid']
            Username = form.cleaned_data['Username']
            Userphone = form.cleaned_data['Userphone']
            Useremail = form.cleaned_data['Useremail']
            c_Userid=request.POST['Userid']
            c_Username=request.POST['Username']
            c_Useremail=request.POST['Useremail']
            c_Userphone=request.POST['Userphone']
            data = CusUsers (Userid= c_Userid , Username= c_Username , Useremail= c_Useremail , Userphone = c_Userphone)
            data.save()
            #Log in user
            user = authenticate(username = username,password = password)
            login(request,user)
            messages.success(request, ("You Have Successfully Registered!"))
            return redirect('home')


    return render(request, 'register.html', {'form':form})

#-----------------------------------------------------------------

#Register Employee

#Save data/POST

def register_employee(request):
    form = EmpSignUpForm()
    if request.method == "POST":
        form = EmpSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            Employeeid = form.cleaned_data['Employeeid']
            Employeename = form.cleaned_data['Employeename']
            Employeephone = form.cleaned_data['Employeephone']
            c_empid=request.POST['Employeeid']
            c_empname=request.POST['Employeename']
            c_empphone=request.POST['Employeephone']
            data = Employee (Employeeid= c_empid , Employeename= c_empname , Employeephone = c_empphone)
            data.save()
            #Log in user
            user = authenticate(username = username,password = password)
            login(request,user)
            messages.success(request, ("You Have Successfully Registered!"))
            return redirect('home')


    return render(request, 'register_emp.html', {'form':form})  

#-----------------------------------------------------------------

#Item

#Save data/POST

def customer_item(request):
    if request.method =='POST':
        i_itemid = request.POST['Itemid']
        i_itemname = request.POST['Itemname']
        i_itemquantity = request.POST['Itemquantity']
        i_itemdescription = request.POST['Itemdescription']
        data = Item (Itemid= i_itemid , Itemname= i_itemname , Itemquantity= i_itemquantity , Itemdescription = i_itemdescription)
        data.save()
        messages.success(request, ("Item Successfully Added!"))
        return render(request,'home.html')
    else:
        return render(request, 'item.html')

#view/GET

def view_order(request):
    alldata = Item.objects.all()
    dict = {
        'alldata':alldata
    }
    return render (request,'vieworder.html',dict)

def update_item(request,Itemid):
    data = Item.objects.get(Itemid = Itemid)
    dict = {
        'data':data
    }
    return render(request,"updateorder.html",dict)

#update/PUT

def update_data(request,Itemid):
    if request.method == 'POST':
        c_itemname = request.POST['Itemname']
        c_itemprice = request.POST['Itemquantity']
        c_itemdescription = request.POST['Itemdescription']
        data = Item.objects.get(Itemid=Itemid)
        data.Itemname = c_itemname
        data.Itemquantity = c_itemprice
        data.Itemdescription = c_itemdescription
        data.save()
        messages.success(request, ("Item Successfully Updated!"))
        return HttpResponseRedirect(reverse("view_order"))
    else:
        return render(request,"updateorder.html")

#delete/DELETE        

def deleteorder(request,Itemid):
    data = Item.objects.get(Itemid = Itemid)
    data.delete()
    messages.success(request, ("Item Successfully Deleted!"))
    return HttpResponseRedirect(reverse("view_order"))

#------------------------------------------------------------------

#Customer

#view/GET

def view_customer(request):
    alldata = User.objects.all()
    dict = {
        'alldata':alldata
    }
    return render (request,'viewcustomer.html',dict)


def update_customer(request,Userid):
    data = User.objects.get(Userid = Userid)
    dict = {
        'data':data
    }
    return render(request,"updatecustomer.html",dict)

#update/PUT

def update_datacustomer(request,Userid):
    if request.method == 'POST':
        u_Username = request.POST['Username']
        u_Useremail = request.POST['Useremail']
        u_Userphone = request.POST['Userphone']
        data = User.objects.get(Userid=Userid)
        data.Username = u_Username
        data.Useremail = u_Useremail
        data.Userphone = u_Userphone
        data.save()
        messages.success(request, ("User Successfully Updated!"))
        return HttpResponseRedirect(reverse("view_customer"))
    else:
        return render(request,"updatecustomer.html")

#delete/DELETE

def deletecustomer(request,Userid):
    data = User.objects.get(Userid = Userid)
    data.delete()
    messages.success(request, ("User Successfully Deleted!"))
    return HttpResponseRedirect(reverse("view_customer"))

#------------------------------------------------------------------

#Employee

#view/GET

def view_employee(request):
    alldata = Employee.objects.all()
    dict = {
        'alldata':alldata
    }
    return render (request,'viewemployee.html',dict)


def update_employee(request,Employeeid):
    data = Employee.objects.get(Employeeid = Employeeid)
    dict = {
        'data':data
    }
    return render(request,"updateemployee.html",dict)

#update/PUT

def update_dataemployee(request,Employeeid):
    if request.method == 'POST':
        e_Employeename = request.POST['Employeename']
        e_Employeephone = request.POST['Employeephone']
        data = Employee.objects.get(Employeeid=Employeeid)
        data.Employeename = e_Employeename
        data.Employeephone = e_Employeephone
        data.save()
        messages.success(request, ("Employee Successfully Updated!"))
        return HttpResponseRedirect(reverse("view_employee"))
    else:
        return render(request,"updateemployee.html")

#delete/DELETE

def deleteemployee(request,Employeeid):
    data = Employee.objects.get(Employeeid = Employeeid)
    data.delete()
    messages.success(request, ("Employee Successfully Deleted!"))
    return HttpResponseRedirect(reverse("view_employee"))

#------------------------------------------------------------------

#Search customer page

#view/GET

def searchpage(request):
    member = User.objects.filter(Q(Userid=request.GET.get('search')))
    return render(request, 'searchpage.html', {'member':member})

#Search order page

#view/GET

def search_order(request):
    query = request.GET.get('search')
    if query:
        orders = Booking.objects.filter(
            models.Q(Userid__Username__icontains=query) |
            models.Q(Itemid__Itemname__icontains=query)
        )
    else:
        orders = None
    return render(request, 'searchorder.html', {'orders': orders})

#------------------------------------------------------------------

#Create order

#Save data/POST

def create_order(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        total_quantity = request.POST['total_quantity']
        date_booking = request.POST['date_booking']
        date_return = request.POST['date_return']
        expire_date = request.POST['expire_date']

        try:
            item = Item.objects.get(Itemid=item_id)
        except Item.DoesNotExist:
            messages.error(request, 'Item with ID {} does not exist'.format(item_id))
            return redirect('create_order')

        booking = Booking(
            Itemid=item,
            Datebooking=date_booking,
            Datereturn=date_return,
            TotalQuantity=total_quantity,  # Use the correct field name 'TotalQuantity'
            ExpireDate=expire_date,  # Use the correct field name 'ExpireDate'
        )
        booking.save()

        # Get the primary key (pk) of the created booking 
        created_booking_pk = booking.pk

        messages.success(request, 'Booking created successfully')
        return redirect('order_detail', pk=created_booking_pk)

    customers = CusUsers.objects.all()
    items = Item.objects.all()
    context = {
        'customers': customers,
        'items': items
    }
    return render(request, 'create_order.html', context)




#------------------------------------------------------------------

#Booking detail

#View/GET

def order_detail(request, pk):
    order = get_object_or_404(Booking, pk=pk)
    context = {'order': order}
    return render(request, 'order_detail.html', context)

#------------------------------------------------------------------

#Booking list

#View/GET

def order_list(request):
    bookings = Booking.objects.all()
    context = {'booking': Booking}
    return render(request, 'order_list.html', {'bookings': bookings})

