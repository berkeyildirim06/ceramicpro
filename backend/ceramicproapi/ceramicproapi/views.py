from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Warranty 
from .serializers import WarrantySerializer

@api_view(['GET'])
def warranty_list(request):
    warranties = Warranty.objects.all()
    serializer = WarrantySerializer(warranties, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def warranty_create(request):
    serializer = WarrantySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def warranty_detail(request, id):
    try:
        warranty = Warranty.objects.get(pk=id)
    except Warranty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = WarrantySerializer(warranty)
    return Response(serializer.data)

@api_view(['PUT'])
def warranty_update(request, id):
    try:
        warranty = Warranty.objects.get(pk=id)
    except Warranty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = WarrantySerializer(warranty, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def warranty_delete(request, pk):
    try:
        warranty = Warranty.objects.get(pk=pk)
    except Warranty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    warranty.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

