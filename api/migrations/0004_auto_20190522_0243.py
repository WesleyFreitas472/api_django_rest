# Generated by Django 2.2.1 on 2019-05-22 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190522_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='acordo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Acordo'),
        ),
    ]
