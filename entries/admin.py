from django.contrib import admin
from .models import Entry
# from .models import Entry_Analytics
 
admin.site.register(Entry) # Регистрируем модель.
# admin.site.register(Entry_Analytics)


class MyModelAdmin(admin.ModelAdmin):
    list_display = ['image']

