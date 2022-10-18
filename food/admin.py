from django.contrib import admin
from .models import Pizza, Kebab
# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceSMALL', 'priceBIG')
admin.site.register(Pizza, PizzaAdmin)


class KebabAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceSMALL', 'priceBIG')
admin.site.register(Kebab, KebabAdmin)