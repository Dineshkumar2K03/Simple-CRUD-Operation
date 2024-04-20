from django.contrib import admin
from crudApp.models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list = ['sno','sname','sclass','saddress']

admin.site.register(student,studentAdmin)