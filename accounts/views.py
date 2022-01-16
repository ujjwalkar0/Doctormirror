from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import doctorresponse,problems,usercatagory,ambulances,location,doctors,file2links,nurses,hospital,chats
from .forms import ProblemsForm,Patients,Doctor,Nurse,Ambulance,Hospital,file2link,chat
from ipware import get_client_ip

def login(request):
    print(f'''
    
    Client's Ip address is: {get_client_ip(request)}
    
    ''')
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
        return render(request, "login.html", {'ip':get_client_ip(request)[0]})
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
        'form': form,
        'notifications': problems.objects.all(),
    }
    return render(request, "home.html", context)

def doctor(request):
    form = Doctor(request.POST,request.FILES)
    if form.is_valid():
        print(form)
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
def hospitals(request):
    form = Hospital(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = Hospital()
    context = {
        'form': form
    }
    return render(request,'hospital.html',context)

def profile(request):
    context = {
        'doctor': doctors.objects.all(),
        'ambulances': ambulances.objects.all(),
        'nurses': nurses.objects.all(),
        'hospitals': hospital.objects.all(),

    }
    return render(request,'profile.html',context)

def chatting(request):
    form = chat(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = chat()
    context = {
        'files': chats.objects.all(),
        'form': form
    }
    return render(request,'chats.html',context)


def files2links(request):
    form = file2link(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        form = file2link()
    context = {
        'files': file2links.objects.all(),
        'form': form
    }
    return render(request,'file2links.html',context)

def locations(request):
    context = {
        'obj_list': doctors.objects.all(),
    }
    return render(request,'cheak/loc.html',context)
def finddoctor(request):
    context = {
        'obj_list': doctors.objects.all(),
    }
    return render(request,'cheak/doctors.html',context)

def notification(request):
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        doctor_id = request.POST['doctor_id']
        abc = request.POST['abc']
        response = request.POST['response']
        myresponse = doctorresponse.objects.create(patient_id=patient_id,doctor_id=doctor_id,abc=abc,response=response)
        myresponse.save()
       
        context = {
        'notifications': problems.objects.all(),
        'some':doctorresponse.objects.all(),
        }
        return render(request, "notification.html", context)
    else:
        context = {
        'notifications': problems.objects.all(),
        'some':doctorresponse.objects.all(),
        }
        return render(request, "notification.html", context)
