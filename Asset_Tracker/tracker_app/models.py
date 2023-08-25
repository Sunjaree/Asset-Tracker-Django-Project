from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class employee(models.Model):

    company_name = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=50)
    employee_email = models.EmailField(max_length=50)
    employee_phone = models.CharField(max_length=10)
    employee_designation = models.CharField(max_length=50)
    employee_department = models.CharField(max_length=50)
    employee_salary = models.IntegerField()
    

    def __str__(self):
        return self.employee_name
    

   
class assets(models.Model):

    company_name = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_id = models.AutoField(primary_key=True)
    asset_name = models.CharField(max_length=50)
    asset_type = models.CharField(max_length=50)
    asset_condition = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    

    def __str__(self):
        return self.asset_name
    


class asset_assigned(models.Model):
    
    company_name = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_assigned_to = models.ForeignKey(employee, on_delete=models.CASCADE)
    asset_checkout_date = models.DateField()
    asset_return_date = models.DateField()
    asset_log= models.CharField(max_length=200)


    

