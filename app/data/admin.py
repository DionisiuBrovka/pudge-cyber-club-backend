from django.contrib import admin
from .models import *

admin.site.site_header = "PUDGE CYBER CLUB"

# Пользователь
# -------------------------------------------------------------------------
@admin.register(AppUser)
class AppUserAdminModel(admin.ModelAdmin):
    list_display = ['username','bonus_balance', 'is_active',]
    list_filter = ['is_active', 'is_staff', 'is_superuser']


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