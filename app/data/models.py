from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Пользователь
# -------------------------------------------------------------------------
class AppUser(AbstractUser):
    bonus_balance = models.FloatField(null=False, blank=True, default=0.0, verbose_name="Балланс бонусов")
    avatar = models.ImageField(null=True, blank=True, verbose_name="Аватарка")

    def __str__(self) -> str:
        return f"Пользователь #{self.id} | {self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


# Клуб
# -------------------------------------------------------------------------
class Club(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название клуба")
    adress = models.CharField(max_length=255, null=False, blank=False, verbose_name="Адресс клуба")

    contacts_phone = models.CharField(max_length=20, null=False, blank=False, verbose_name="Контактный номер")
    contacts_instagram = models.URLField(null=True, blank=True, verbose_name="Ссылка на инсту")
    contacts_telegram = models.URLField(null=True, blank=True, verbose_name="Ссылка на телегу")

    map_link = models.URLField(null=False, blank=False, verbose_name="Ссылка на карту")
    map_lat = models.FloatField(null=False, blank=False, verbose_name="Долгота на карте")
    map_lng = models.FloatField(null=False, blank=False, verbose_name="Широта на карте")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"


# Уровень компьютера
# -------------------------------------------------------------------------
class PCLevel(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Название")

    desc = models.TextField(null=True, blank=True, verbose_name="Описание")

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        verbose_name = "Уровень компьютера"
        verbose_name_plural = "Уровни компьютера"


# Компьютер
# -------------------------------------------------------------------------
class PC(models.Model):
    club = models.ForeignKey( Club, models.CASCADE, null=False, blank=False, verbose_name="Клуб")
    pc_level = models.ForeignKey( PCLevel, models.CASCADE, null=False, blank=False, verbose_name="Тип компьютера")

    num = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name="Номер компьютера") 

    def __str__(self) -> str:
        return f"Компьютер #{self.id} | Номер {self.num} Клуб {self.club.title} "

    class Meta:
        verbose_name = "Компьютер"
        verbose_name_plural = "Компьютеры"