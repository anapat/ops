from django.contrib import admin

from .models import Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'user', 'ip', 'memory', 'sort', 'datetime_create')
