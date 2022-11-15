from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import FieldDataSerializer, FieldDataFileSerializer, SpeciesFileSerlizer, FieldDataHieghestTree, SpeciesSerializer
from .models import FieldData, Species
import pandas as pd
import io, csv
from django.shortcuts import get_object_or_404

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
    # store query param in a variable
    selected_year = request.query_params.get('year_monitored')
    
    # get the first five entries in the query set
    field_data = FieldData.objects.values('individual_tree_id', 'height').filter(year_monitored = selected_year).order_by('-height')[:5]
    
    # create serializer
    serializer = FieldDataHieghestTree(field_data, many = True)

    # create final output
    final_output = {"year": selected_year, "highest_trees": serializer.data}
    return Response(final_output)

@api_view(['GET'])
def getSpecies(request):
    # query distinct methods for data
    species = Species.objects.all()
    
    #serialize the data
    serializer = SpeciesSerializer(species, many = True)
    return Response(serializer.data)


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