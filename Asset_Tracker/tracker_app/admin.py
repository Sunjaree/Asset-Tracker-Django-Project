from django.contrib import admin
from tracker_app.models import employee, assets, asset_assigned

# Register your models here.

admin.site.register(employee)
admin.site.register(assets)
admin.site.register(asset_assigned)

