from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import problems,usercatagory,ambulances,doctors,nurses,hospital,location
from .forms import ProblemsForm,Patients,Doctor,Nurse,Ambulance,Hospital

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            #messages.info(request, 'Logging in')
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Login Invalid')
            return redirect('/')
    else:
        return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'User Created')
                return redirect('/')
                print("User Created")
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
    else:
        return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return render(request, "home.html")
def patients(request):
    form = Patients(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = Patients()
    context = {
        'form': form
    }
    return render(request, "patient.html", context )
def home(request):
    form = ProblemsForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = ProblemsForm()
    context = {
        'form': form
    }
    return render(request, "home.html", context)
'''
def create_profile(request):
    return render(request, "cuseas.html")
def view_profile(request):
    return render(request, "vuseas.html")
def edit_profile(request):
    return render(request, "euseas.html")
def usingas(request):
    context={
        "datas":usercatagory.objects.all()
    }
    return render(request,'a.html',context)
def home(request):
    return render(request,'home.html')
'''
def doctor(request):
    form = Doctor(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = Doctor()
    context = {
        'obj_list': doctors.objects.all(),
        'form': form,

    }
    return render(request,'Doctor.html',context)
def nurse(request):
    form = Nurse(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = Nurse()
    context = {
        'obj_list': nurses.objects.all(),
        'form': form
    }
    return render(request,'Nurse.html',context)
def ambulance(request):
    form = Ambulance(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = Ambulance()
    context = {
        'obj_list': ambulances.objects.all(),
        'form': form,
        
    }
    return render(request,'ambulance.html',context)

def add(request):
    form = Ambulance(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = Ambulance()
    context = {
        'obj_list': ambulances.objects.all(),
        'form': form,
        
    }
    return render(request,'add.html',context)

def hospitals(request):
    form = Hospital(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = Hospital()
    context = {
        'obj_list': hospital.objects.all(),
        'form': form
    }
    return render(request,'hospital.html',context)

def locations(request):
    if request.method == 'POST':
        username = request.POST['username']
        catagory = request.POST['catagory']
        Latitude = request.POST['Latitude']
        Longitude = request.POST['Longitude']
        loc = location.objects.create(username=username,catagory=catagory,Latitude=Latitude,Longitude=Longitude)
        loc.save()
        return render(request,'cheak/loc.html')
    else:
        return render(request,'cheak/loc.html')
