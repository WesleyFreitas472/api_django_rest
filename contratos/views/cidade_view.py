from ..serializers import CidadeSerializer
from ..serializers import EstadoSerializer
from ..models import Estado
from ..models import Cidade
from rest_framework import generics

from django.shortcuts import render

class EstadoView(generics.ListCreateAPIView):
	queryset = Estado.objects.all()
	serializer_class = EstadoSerializer

class CidadeView(generics.ListCreateAPIView):
	queryset = Cidade.objects.all()
	serializer_class = CidadeSerializer

class EstadoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Estado.objects.all()
	serializer_class = EstadoSerializer
