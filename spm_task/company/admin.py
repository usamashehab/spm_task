from django.contrib import admin
from .models import Company, Startup, SmallBusiness, Corporate


admin.site.register(Company)
admin.site.register(Corporate)
admin.site.register(SmallBusiness)
admin.site.register(Startup)
