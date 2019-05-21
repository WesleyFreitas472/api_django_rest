from __future__ import unicode_literals

from django.db import models

class Agencia(models.Model):
	num = models.CharField(max_length=200)

	class Meta:
		db_table = 'agencia'