from django.shortcuts import render
from rest_framework import generics
from rest_framework import views
from api.models import Cliente
from api.models import Acordo
from api.models import Parcela
from api.serializers import ClienteSerializer
from api.serializers import AcordoListSerializer
from api.serializers import AcordoCreateSerializer
from api.serializers import ParcelaSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import generics
from django_filters import rest_framework as filters


class ParcelaCreate(generics.CreateAPIView):
	queryset = Parcela.objects.all()
	serializer_class = ParcelaSerializer

class ParcelaDestroy(generics.DestroyAPIView):
	queryset = Parcela.objects.all()
	serializer_class = ParcelaSerializer

class ParcelaUpdate(generics.UpdateAPIView):
	queryset = Parcela.objects.all()
	serializer_class = ParcelaSerializer

class AcordoCreate(generics.CreateAPIView):
	queryset = Acordo.objects.all()
	serializer_class = AcordoCreateSerializer


			

class AcordoDetail(generics.RetrieveAPIView):
	queryset = Acordo.objects.all()
	serializer_class = AcordoListSerializer

class AcordoList(generics.ListAPIView):

#	queryset = get_queryset()
#	queryset = Acordo.objects.all()
	serializer_class = AcordoListSerializer
	
	def get_queryset(self):
		acordo = Acordo.objects.all()
		parcelas = Parcela.objects.filter(acordo=acordo)
		acordo.parcelas = parcelas
		print(acordo)
		return acordo

	

class ClienteCreate(generics.CreateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	
class ClienteList(generics.ListAPIView):

	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated, )
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	 

class ClienteDetail(generics.RetrieveAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	authentication_classes = [SessionAuthentication]
	permission_classes = (IsAuthenticated, )

class ClienteUpdate(generics.UpdateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	
class ClienteDelete(generics.DestroyAPIView):
	serializer_class = ClienteSerializer
	queryset = Cliente.objects.all()


