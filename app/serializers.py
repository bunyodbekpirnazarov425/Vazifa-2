from rest_framework import serializers
from .models import Klass, Mehmonxona, Travle

class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = '__all__'

    def create(self, validated_data):
        return Klass.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nomi = validated_data.get('nomi', instance.nomi)
        instance.narxi = validated_data.get('narxi', instance.narxi)
        instance.save()
        return instance

class MehmonxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mehmonxona
        fields = '__all__'

    def create(self, validated_data):
        return Mehmonxona.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nomi = validated_data.get('nomi', instance.nomi)
        instance.yulduzlar_soni = validated_data.get('yulduzlar_soni', instance.yulduzlar_soni)
        instance.narxi = validated_data.get('narxi', instance.narxi)
        instance.save()
        return instance

class TravleSerializer(serializers.ModelSerializer):
    klass = KlassSerializer()
    mehmonxona = MehmonxonaSerializer()

    class Meta:
        model = Travle
        fields = '__all__'

    def create(self, validated_data):
        klass_data = validated_data.pop('klass')
        mehmonxona_data = validated_data.pop('mehmonxona')
        klass = Klass.objects.create(**klass_data)
        mehmonxona = Mehmonxona.objects.create(**mehmonxona_data)
        travle = Travle.objects.create(klass=klass, mehmonxona=mehmonxona, **validated_data)
        return travle

    def update(self, instance, validated_data):
        klass_data = validated_data.pop('klass', None)
        mehmonxona_data = validated_data.pop('mehmonxona', None)

        if klass_data:
            klass_instance = instance.klass
            klass_instance.nomi = klass_data.get('nomi', klass_instance.nomi)
            klass_instance.narxi = klass_data.get('narxi', klass_instance.narxi)
            klass_instance.save()

        if mehmonxona_data:
            mehmonxona_instance = instance.mehmonxona
            mehmonxona_instance.nomi = mehmonxona_data.get('nomi', mehmonxona_instance.nomi)
            mehmonxona_instance.yulduzlar_soni = mehmonxona_data.get('yulduzlar_soni', mehmonxona_instance.yulduzlar_soni)
            mehmonxona_instance.narxi = mehmonxona_data.get('narxi', mehmonxona_instance.narxi)
            mehmonxona_instance.save()

        instance.nomi = validated_data.get('nomi', instance.nomi)
        instance.izoh = validated_data.get('izoh', instance.izoh)
        instance.muddati = validated_data.get('muddati', instance.muddati)
        instance.narxi = validated_data.get('narxi', instance.narxi)
        instance.save()
        return instance
