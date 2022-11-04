from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Druzyna
from Druzyna.models import Druzyna
from Osoby.serializers import DruzynaSerializer
druzyna = Druzyna(nazwa='Waleczne Serca', kraj='PL')
druzyna.save()

serializerDruzyna = DruzynaSerializer(druzyna) 
serializerDruzyna.data

druzynaContent = JSONRenderer().render(serializerDruzyna.data)

import io

stream = io.BytesIO(druzynaContent)
data = JSONParser().parse(stream)

deserializer = DruzynaSerializer(data=data)

deserializer.is_valid()
deserializer.errors
deserializer.fields
deserializer.validated_data
deserializer.save()
deserializer.data

# Osoby
from Osoby.models import Osoba
from Osoby.serializers import OsobaSerializer

osoba = Osoba(imie='Edmund', nazwisko='Trąbka', data_dodania='2022-11-04', druzyna=druzyna)

osoba.save()

serializerOsoba = OsobaSerializer(osoba)   
serializerOsoba.data

OsobaContent = JSONRenderer().render(serializerOsoba.data)
OsobaContent

import io

stream = io.BytesIO(OsobaContent)
data = JSONParser().parse(stream)

deserializer = OsobaSerializer(data=data)

deserializer.is_valid()
deserializer.errors
deserializer.fields
deserializer.validated_data
deserializer.save()
deserializer.data