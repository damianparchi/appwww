from appka.models import Osoba
from appka.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


osoba = Osoba(name='Adam', miesiac_dodania=1)

osoba.save()

serializer = PersonSerializer(osoba)
serializer.data
