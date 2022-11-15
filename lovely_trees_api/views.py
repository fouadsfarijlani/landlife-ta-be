from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import FieldDataSerializer, FieldDataFileSerializer, SpeciesFileSerlizer, FieldDataHieghestTree, SpeciesSerializer
from .models import FieldData, Species
import pandas as pd
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Count

@api_view(['GET'])
def get_data(request):
    field_data = FieldData.objects.all()
    serializer = FieldDataSerializer(field_data, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = FieldDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getHighestTree(request):
    selected_year = request.query_params.get('year_monitored')
    field_data = FieldData.objects.values('individual_tree_id', 'height').filter(year_monitored = selected_year).order_by('-height')[:5]
    serializer = FieldDataHieghestTree(field_data, many = True)
    final_output = {"year": selected_year, "highest_trees": serializer.data}
    return Response(final_output)

@api_view(['GET'])
def getSpecies(request):
    species = Species.objects.all()
    serializer = SpeciesSerializer(species, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getBestMethodForSpecies(request):
    selected_species = request.query_params.get('species_id')
    method_avg = FieldData.objects.all().filter(species_id = selected_species).aggregate(Avg('health'))
    species_data = Species.objects.all().filter(tree_species_id = selected_species)
    method_count = FieldData.objects.values('method').annotate(total = Count('method')).order_by('-total')[:1][0]
    trees_with_methods = FieldData.objects.values('individual_tree_id', 'year_monitored', 'health').filter(method = method_count['method'])
    
    return Response({'tree_species_id': selected_species, 'best_method': method_count['method'], "health_avg": method_avg['health__avg']})


class UploadSpeciesFileView(generics.CreateAPIView):
    '''
        A class to upload Species csv files and parse them using pandas
    '''

    serializer_class = SpeciesFileSerlizer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Species(
                tree_species_id = row['tree_species_id'],
                latin_name = row['latin_name']
            )
            new_file.save()
        return Response({'status' : 'success'})
class UploadFieldDataFileView(generics.CreateAPIView):
    '''
        A class to upload Species csv files and parse them using pandas
    '''

    serializer_class = FieldDataFileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        reader.fillna(None, method='backfill',inplace=True)
        for _, row in reader.iterrows():
            new_file = FieldData(
                individual_tree_id = row['individual_tree_id'],
                species_id = get_object_or_404(Species, pk=row['species_id']),
                method = row['method'],
                height = row['height'],
                health = row['health'],
                year_monitored = row['year_monitored'],
            )
            new_file.save()
        return Response({'status' : 'success'})