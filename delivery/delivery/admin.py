from django.contrib import admin
from . import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(models.Item)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(models.Leg)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('fromId', 'toId',)

@admin.register(models.Route)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('currentLocation',)

@admin.register(models.Location)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(models.Order)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',)
