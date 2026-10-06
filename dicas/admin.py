from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Dica


@admin.register(Dica)
class DicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_criacao')
    search_fields = ('titulo', 'categoria')
