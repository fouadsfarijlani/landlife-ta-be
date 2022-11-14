from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FieldDataSerializer

@api_view(['GET'])
def get_data(request):
    test = {
        'name': 'Test',
        'something': 'hi'
    }
    return Response(test)

@api_view(['POST'])
def addData(request):
    serializer = FieldDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)