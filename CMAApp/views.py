from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import JoinUsForm
from .models import JoinUs, Admin, Car, Product
from .forms import CarForm, ProductForm
from django.contrib.auth.decorators import login_required



# Create your views here.
#Main page
def indexpage(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def joinus(request):
    form = JoinUsForm()
    if request.method == "POST":
        form = JoinUsForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully Registered"
            return render(request, "joinussucc.html", {"msg": msg})
        else:
            msg = "Registration Failed. Please check the form for errors."
            return render(request, "joinus.html", {"form": form, "msg": msg})
    return render(request, "joinus.html", {"form": form})

def checkuserlogin(request):
    emailid=request.POST["emailid"]
    pwd=request.POST["password"]

    flag=JoinUs.objects.filter( Q(email=emailid) & Q(password=pwd) )
    print(flag)

    if flag:
        user=JoinUs.objects.get(email=emailid)
        print(user)
        print(user.id,user.fullname)  #other fields
        request.session["uname"]=user.username
        return render(request,"userhome.html",{"uname":user.username})
    else:
        msg="Login Failed"
        return render(request, "login.html",{"msg":msg})

def joinussucc(request):
    return render(request,"joinussucc.html")

def home(request):
    return render(request,"home.html")


#user home
def userhome(request):
    return render(request,"userhome.html")
def userlogout(request):
    return render(request,"login.html")

#Admin
def adminlogin(request):
    return render(request,"adminlogin.html")


def checkadminlogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")
        if not uname or not pwd:
            msg = "Username and password are required."
            return render(request, "adminhome.html", {"msg": msg})
        flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))
        print(flag)
        if flag.exists():
            admin = Admin.objects.get(username=uname)
            print(admin)
            request.session["auname"] = admin.username
            return render(request, "adminhome.html", {"auname": admin.username})
        else:
            msg = "Login Failed"
            return render(request, "adminlogin.html", {"msg": msg})
    return render(request, "adminlogin.html")

def adminhome(request):
    return render(request,"adminhome.html")


def addproduct(request):
    form = ProductForm()
    if request.method == "POST":
        formdata = ProductForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Product Added Successfully"
            return render(request, "addproduct.html", {"productform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addproduct.html", {"productform": form, "msg": msg})
    return render(request,"addproduct.html",{"productform":form})

def addcar(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg = "Car Details Added Successfully"
            return render(request, "addcar.html", {"carform": form, "msg": msg})
        else:
            msg = "Failed to Add Car Details"
            # Pass form.errors to the template
            return render(request, "addcar.html", {"carform": form, "msg": msg, "errors": form.errors})
    return render(request, "addcar.html", {"carform": form})

def viewallcars(request):
    carlist = Car.objects.all()
    count = Car.objects.count()
    return render(request,"viewallcars.html",{"carlist":carlist,"count":count})

def displayallcars(request):
    # Initialize the car list
    if request.method == "POST":
        # Get the name from the POST request, default to empty string if not found
        name = request.POST.get("name", "")
        print(f"Searching for cars with name containing: {name}")
        # Filter cars by name, ensuring no duplicates
        carlist = Car.objects.filter(name__icontains=name).distinct()
    else:
        # Fetch all cars from the database, ensuring no duplicates
        carlist = Car.objects.all().distinct()

    # Return the render with the list of cars
    return render(request, "displayallcars.html", {"carlist": carlist})

