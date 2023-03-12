from django.contrib import admin
from . models import Room,Message

# Register your models here.

@admin.register(Room)

class RoomAdmin(admin.ModelAdmin):
    list_display = ("name","id")
    search_fields = ("name","")
admin.site.register(Message)