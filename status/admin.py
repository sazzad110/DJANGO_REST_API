from django.contrib import admin
from status.models import Status

# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ('text','created_at','user')     # show this 

admin.site.register(Status, StatusAdmin)
