from django.contrib import admin
from.models import Hiretuber

# Register your models here.



class hireAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','state')
    list_display_link=('first_name','email',)
    search_fields=('name',)
    list_filter=('state',)



admin.site.register(Hiretuber,hireAdmin)    