from __future__ import unicode_literals

from django.db import models

class Regional(models.Model):

	regiao = models.CharField(max_length=200,null=True)

	class Meta:
		db_table = 'regional'