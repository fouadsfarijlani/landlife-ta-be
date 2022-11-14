from rest_framework import serializers
from lovely_trees_api.models import Species, FieldData

class FieldDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldData
        fields = '__all__'


class FieldDataFileSerializer(serializers.Serializer):
    file = serializers.FileField()

class SpeciesFileSerlizer(serializers.Serializer):
    file = serializers.FileField()