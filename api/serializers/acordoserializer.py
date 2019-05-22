from rest_framework import serializers
from api.models import Acordo
from api.models import Parcela
from api.serializers import ClienteSerializerId


class ParcelaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Parcela
		fields = ('valor_parcela','data_vencimento')


class AcordoListSerializer(serializers.ModelSerializer):

	parcela = ParcelaSerializer(many=True,required = False)

	class Meta:

		model = Acordo
		#fields = ('id','data_acordo','valor_original','valor_acordado','desconto','contratante','parcela',)
		fields = '__all__'
		#read_only_fields = ('parcelas',)
		
		#depth = 1
	


#cria reverse relationship

class AcordoCreateSerializer(serializers.ModelSerializer):

	parcela = ParcelaSerializer(many=True)
	class Meta:

		model = Acordo
		fields = ('id','data_acordo','valor_original','valor_acordado','desconto','contratante','parcela',)		
		#depth = 1
	def create(self,dados):
		print(dados)
		parcelas = dados.pop('parcela')
		print(parcelas)
		acordo = Acordo.objects.create(**dados)
		acordo.parcelas = []
		for parcela in parcelas:
			Parcela.objects.create(**parcela,acordo=acordo)
			acordo.parcelas.append(parcela)
		print('AQUI')
		return acordo



	



'''
{
	"data_acordo": "2019-05-01",
	"valor_original": 2000,
	"valor_acordado": 1000,
	"desconto": 50,
	"contratante": 1,
	"parcela": [
		{
			"data_vencimento": "2019-06-01",
			"valor_parcela": "50"			
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		},
		{
			"data_vencimento": "2019-07-01",
			"valor_parcela": "500"		
		}
	]
}
'''
