from django.contrib import admin
from tracker_app.models import Employee, Assets, AssetAssigned

# Register your models here.

admin.site.register(Employee)
admin.site.register(Assets)
admin.site.register(AssetAssigned)

