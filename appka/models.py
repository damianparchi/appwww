from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class MONTHS(models.TextChoices):
        STYCZEN = '1', _('STYCZEN')
        LUTY = '2', _('LUTY')
        MARZEC = '3', _('MARZEC')
        KWIECIEN = '4', _('KWIECIEN')
        MAJ = '5', _('MAJ')
        CZERWIEC = '6', _('CZERWIEC')
        LIPIEC = '7', _('LIPIEC')
        SIERPIEN = '8', _('SIERPIEN')
        WRZESIEN = '9', _('WRZESIEN')
        PAZDZIERNIK = '10', _('PAZDZIERNIK')
        LISTOPAD = '11', _('LISTOPAD')
        GRUDZIEN = '12', _('GRUDZIEN')

class Druzyna(models.Model):
    class Kraj(models.TextChoices):
        POLSKA = "PL", _("Polska")
        USA = "US", _("Stany Zjednoczone")
        NIEMCY = "DE", _("Niemcy")
        FRANCJA = "FR", _("Francja")
        ANGLIA = "EN", _("Anglia")

    nazwa = models.CharField(max_length = 50)
    kraj = models.CharField(max_length = 2, choices = Kraj.choices)

    def __str__(self):
        return str(self.nazwa) + " (" + str(self.kraj) + " )"


class Osoba(models.Model):
    imie = models.CharField(max_length = 50)
    nazwisko = models.CharField(max_length = 50)
    miesiac = models.CharField(max_length = 2, choices = MONTHS.choices, default = MONTHS.STYCZEN)
    data_dodania = models.DateField(default=datetime.now())
    druzyna = models.ForeignKey(Druzyna, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        return str(self.imie) + " (" + str(self.nazwisko)

    class Meta:
        ordering = ["nazwisko"]