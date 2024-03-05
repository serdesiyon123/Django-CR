from django.contrib import admin
from .models import DB

class store_id(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(DB, store_id)
