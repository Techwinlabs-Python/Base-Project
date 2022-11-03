from atexit import register
from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    ordering = ('date_joined', )
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff')
