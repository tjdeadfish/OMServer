from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Manager)
admin.site.register(DBA)
admin.site.register(State)
admin.site.register(DataBase)
admin.site.register(Task)