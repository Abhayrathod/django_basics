from django.contrib import admin
from .models import Students

# admin.site.register(Students)

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display: ['id','name','roll','city']