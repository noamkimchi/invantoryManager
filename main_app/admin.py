from django.contrib import admin
from main_app.models import Item, Kit, KitContains

admin.site.register(Item)
admin.site.register(Kit)
admin.site.register(KitContains)