from django.contrib import admin
from home import models
# Register your models here.
@admin.register(models.Listing)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }