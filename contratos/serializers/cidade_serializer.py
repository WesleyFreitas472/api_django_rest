from rest_framework import serializers
from contratos.models import Cidade
from contratos.models import Estado

class EstadoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Estado
		fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):

	estado = EstadoSerializer(many=False,read_only=False)

	class Meta:
		model = Cidade
		fields = '__all__'

