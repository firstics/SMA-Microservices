from django.contrib import admin
from record.models import Cashier,Manager,Store,DailyRecord
# Register your models here.

admin.site.register(Cashier)
admin.site.register(Manager)
admin.site.register(Store)
admin.site.register(DailyRecord)