from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User , auth
# Create your views here.

def signup(request):
    if request.method == 'post':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email_id=request.POST['email_id']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user = User.objects.create_user(email_id=email_id,password1=password1,password2=password2,first_name=first_name,last_name=last_name)
        user.save()
        print("User Created")
      #  return redirect('/')

    else:
        return render(request,'doctor.html')
