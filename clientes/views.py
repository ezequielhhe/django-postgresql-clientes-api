from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClienteSerializer
from .models import Cliente

@api_view(['GET'])
def obtenerTodo(request):
    clientes = Cliente.objects.all()
    serializer = ClienteSerializer(clientes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def obtenerPorId(request, pk):
    cliente = Cliente.objects.get(id = pk)
    serializer = ClienteSerializer(cliente, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def guardar(request):
    serializer = ClienteSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def editar(request, pk):
    cliente = Cliente.objects.get(id = pk)
    serializer = ClienteSerializer(instance = cliente, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def borrar(request, pk):
    cliente = Cliente.objects.get(id = pk)
    cliente.delete()
    return Response(status = status.HTTP_200_OK)
