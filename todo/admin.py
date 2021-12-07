from django.contrib import admin
from .models import ToDoApp
# Register your models here.
class ChangeTable(admin.ModelAdmin):
    list_display=["author","desc","datetime"]
admin.site.register(ToDoApp,ChangeTable)