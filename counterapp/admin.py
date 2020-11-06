from django.contrib import admin
from .models import NewsData,Category,Message,EmployeeModel

admin.site.register(NewsData)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(EmployeeModel)