from django.contrib import admin
from .models import BadgeCategory, Badge, Dashboard
# Register your models here.
admin.site.register(BadgeCategory)
admin.site.register(Badge)
admin.site.register(Dashboard)