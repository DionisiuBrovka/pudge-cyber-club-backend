from django.contrib import admin
from .models import *

# Register your models here.

# Пользователь
# -------------------------------------------------------------------------
@admin.register(AppUser)
class AppUserAdminModel(admin.ModelAdmin):
    list_display = ['username', 'is_active', 'is_staff', 'is_superuser']


# Клуб
# -------------------------------------------------------------------------
@admin.register(Club)
class ClubAdminModel(admin.ModelAdmin):
    list_display = ['title', 'adress']


# Компьютер
# -------------------------------------------------------------------------
@admin.register(PC)
class PCAdminModel(admin.ModelAdmin):
    list_display = ['num', 'club', 'pc_level']
    list_filter = ['club', 'pc_level']


# Уровень компьютера
# -------------------------------------------------------------------------
@admin.register(PCLevel)
class PCLevelAdminModel(admin.ModelAdmin):
    pass