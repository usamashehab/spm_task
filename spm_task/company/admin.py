from django.contrib import admin
from .models import Company, Startup, SmallBusiness, Corporate


admin.site.registerJ(Company)
admin.site.registerJ(Corporate)
admin.site.registerJ(SmallBusiness)
admin.site.registerJ(Startup)
