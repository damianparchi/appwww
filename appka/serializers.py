from rest_framework import serializers
from .models import Osoba, Druzyna, MONTHS


class OsobaSerializer(serializers.Serializer):


    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    miesiac_dodania = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.druzyna = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance

class DruzynaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True)
    kraj = serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance . kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance