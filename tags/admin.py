from django.contrib import admin
from .models import Tags

# Register models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']
