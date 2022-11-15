from rest_framework import serializers
from lovely_trees_api.models import Species, FieldData

class FieldDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldData
        fields = '__all__'

class FieldDataHieghestTree(serializers.ModelSerializer):
    class Meta:
        model = FieldData
        fields = ['individual_tree_id', 'height']

class FieldDataFileSerializer(serializers.Serializer):
    file = serializers.FileField()

class SpeciesFileSerlizer(serializers.Serializer):
    file = serializers.FileField()

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'
