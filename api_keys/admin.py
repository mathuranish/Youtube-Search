from django.contrib import admin
from .models import APIKeys

# Register your models here.


@admin.register(APIKeys)
class APIkeysAdmin(admin.ModelAdmin):
    list_display = ["id", "key", "created"]

    list_filter = ["created"]
