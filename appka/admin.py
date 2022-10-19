from django.contrib import admin
from .models import Osoba, Druzyna
# Register your models here.
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'miesiac', 'data_dodania', 'druzyna')
    list_filter = ["druzyna", "data_dodania"]
admin.site.register(Osoba, OsobaAdmin)


class DruzynaAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'kraj')
    list_filter = ['kraj']
admin.site.register(Druzyna, DruzynaAdmin)
# Register your models here.
