from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages

# Create your views here.




# def index(request):
#     return HttpResponse("This is the tracker_app homepage")  


 

def handle_signup(request):

    if request.method == 'POST':

        company_name = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(company_name=company_name).count()==1:
            messages.warning(request, "This company account already exists, Please login")
            return redirect('tracker_app')

        my_user = User.objects.create_user(company_name, password)
        my_user.save()

        messages.success(request,"Your account has been created successfully!!!")
        return redirect('tracker_app')

    else:
        return HttpResponse("404-Not Found")




def handle_login(request):

    if request.method=='POST':

        login_username = request.POST['login_username']
        login_password = request.POST['login_password']

        user = authenticate(username=login_username,password=login_password)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('tracker_app')
        else:
            messages.warning(request,"Invalid credentials, Please try again")
            return redirect('tracker_app')

    else:
        return HttpResponse("404-Not Found") 




def handle_logout(request):
    logout(request)
    messages.success(request,"Successfully Loggged Out")
    return redirect('tracker_app')





