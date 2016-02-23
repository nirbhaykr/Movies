from django.contrib import admin
from Data.models import Category,Movies

# Register your models here.

model_list = [Category,Movies]

admin.site.register(model_list)