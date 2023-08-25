from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from tracker_app.models import Employee, Assets, AssetAssigned


# Create your views here.




def index(request):
    return render(request,'index.html')


 
# function for signup of a company
def handle_signup(request):

    if request.method == 'POST':

        company_name = request.POST['username']
        password = request.POST['password']

        # check if the company account already exists
        if User.objects.filter(company_name=company_name).count()==1:
            messages.warning(request, "This company account already exists, Please login")
            return redirect('tracker_app')

        # create a new company account
        my_user = User.objects.create_user(company_name, password)
        my_user.save()

        messages.success(request,"Your account has been created successfully!!!")
        return redirect('tracker_app')

    else:
        # if the request is not POST then return 404 error
        return HttpResponse("404-Not Found")



# function for login of a company
def handle_login(request):

    if request.method=='POST':

        login_username = request.POST['login_username']
        login_password = request.POST['login_password']

        # check if the company account exists or not
        user = authenticate(username=login_username,password=login_password)

        # if the company account exists then login the company
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('tracker_app')
        else:
            messages.warning(request,"Invalid credentials, Please try again")
            return redirect('tracker_app')

    else:
        return HttpResponse("404-Not Found") 



# function for logout of a company
def handle_logout(request):
    logout(request)
    messages.success(request,"Successfully Loggged Out")
    return redirect('tracker_app')


# function for adding an employee
def add_employee(request):
    
    company = request.user

    # check if the company is logged in or not
    if request.user.is_authenticated:
        if request.method == 'POST':

            employee_name = request.POST['employee_name']
            employee_email = request.POST['employee_email']
            employee_phone = request.POST['employee_phone']
            employee_designation = request.POST['employee_designation']
            employee_department = request.POST['employee_department']
            employee_salary = request.POST['employee_salary']

            # create a new employee
            employee = Employee(company_name = company, 
                                employee_name = employee_name, 
                                employee_email = employee_email, 
                                employee_phone = employee_phone, 
                                employee_designation = employee_designation, 
                                employee_department = employee_department, 
                                employee_salary = employee_salary)
            employee.save()
            messages.success(request,"Employee added successfully")
            return redirect('tracker_app')
        


# function for adding an asset
def add_assets(request):
    
    company = request.user

    if request.user.is_authenticated:
        if request.method == 'POST':

            asset_name = request.POST['asset_name']
            asset_type = request.POST['asset_type']
            asset_condition = request.POST['asset_condition']
            is_available = request.POST['is_available']

            # create a new asset
            asset = Assets(company_name = company, 
                                asset_name = asset_name, 
                                asset_type = asset_type, 
                                asset_condition = asset_condition, 
                                is_available = is_available)
            asset.save()
            messages.success(request,"Asset added successfully")
            return redirect('tracker_app')
        


# function for assigning an asset to an employee
def assign_assets(request):
        
        company = request.user
    
        if request.user.is_authenticated:
            if request.method == 'POST':
    
                asset_assigned_to = request.POST['asset_assigned_to']
                asset_checkout_date = request.POST['asset_checkout_date']
                asset_return_date = request.POST['asset_return_date']
                asset_log = request.POST['asset_log']
    
                # assign an asset to an employee
                asset_assigned = AssetAssigned(company_name = company, 
                                    asset_assigned_to = asset_assigned_to, 
                                    asset_checkout_date = asset_checkout_date, 
                                    asset_return_date = asset_return_date, 
                                    asset_log = asset_log)
                asset_assigned.save()
                messages.success(request,"Asset assigned successfully")
                return redirect('tracker_app')
            


# function for viewing all the assigned assets
def view_assigned_assets(request):
    company = request.user
    if request.user.is_authenticated:
        # check if the request is GET or not
        if request.method == 'GET':
            # get all the assigned assets of a company
            asset = AssetAssigned.objects.filter(company_name=company)
            return render(request, 'view_asset.html', {'asset':asset})
        else:
            return HttpResponse("404-Not Found")











