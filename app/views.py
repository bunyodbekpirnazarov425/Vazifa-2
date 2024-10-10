from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Klass, Mehmonxona, Travle
from .serializers import KlassSerializer, MehmonxonaSerializer, TravleSerializer

class KlassAPIView(APIView):
    def get(self, request):
        klasslar = Klass.objects.all()
        serializer = KlassSerializer(klasslar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = KlassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        klass = Klass.objects.get(pk=pk)
        serializer = KlassSerializer(klass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        klass = Klass.objects.get(pk=pk)
        klass.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MehmonxonaAPIView(APIView):
    def get(self, request):
        mehmonxonalar = Mehmonxona.objects.all()
        serializer = MehmonxonaSerializer(mehmonxonalar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MehmonxonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        mehmonxona = Mehmonxona.objects.get(pk=pk)
        serializer = MehmonxonaSerializer(mehmonxona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mehmonxona = Mehmonxona.objects.get(pk=pk)
        mehmonxona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TravleAPIView(APIView):
    def get(self, request):
        travlelar = Travle.objects.all()
        serializer = TravleSerializer(travlelar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TravleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        travle = Travle.objects.get(pk=pk)
        serializer = TravleSerializer(travle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        travle = Travle.objects.get(pk=pk)
        travle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
