from django.contrib import admin
from . import models


@admin.register(models.UserProfile)
class adminUserProfile(admin.ModelAdmin):
    list_display=['first_name','last_name']
    ordering=['user__first_name','user__last_name']
    list_select_related=['user']
@admin.register(models.Property)
class AdminProp(admin.ModelAdmin):
    list_display=['title','price','adress','area','state','type_propriete']
    list_editable=['price']
    ordering=['title']
    list_per_page=10
    search_fields=['title']


@admin.register(models.Apartment)
class AdminAppar(admin.ModelAdmin):
    list_display=['title','price','adress','area','state','rooms','bathrooms','floors','waterfront','view','year_built','year_renovted']
    list_editable=['price']
    ordering=['title']
    list_per_page=10
    search_fields=['title']



@admin.register(models.Villa)
class AdminVill(admin.ModelAdmin):
    list_display=['title','price','adress','area','state','rooms','bathrooms','garden','pool','floors','year_built']
    list_editable=['price']
    ordering=['title']
    list_per_page=10
    search_fields=['title']


@admin.register(models.Ground)
class AdminTerrain(admin.ModelAdmin):
    list_display=['title','price','adress','area','state','Ground_type']
    list_editable=['price']
    ordering=['title']
    list_per_page=10
    search_fields=['title']



@admin.register(models.Annonce)
class Adminannoncen(admin.ModelAdmin):
    list_display=['publication_date','Property','Customer']


@admin.register(models.Favoris)
class AdminFavoris(admin.ModelAdmin):
    list_display=['Customer','Annonce']


