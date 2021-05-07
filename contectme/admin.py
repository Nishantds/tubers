from django.contrib import admin
from .models import ContectHere

# Register your models here.
class  conectAdmin(admin.ModelAdmin):
    list_display=('full_name','email','company_name')
    list_display_link=('full_name','email',)
    search_fields=('name',)
    list_filter=('company_name',)


admin.site.register(ContectHere, conectAdmin)