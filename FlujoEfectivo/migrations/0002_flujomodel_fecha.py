# Generated by Django 4.0.3 on 2022-03-15 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlujoEfectivo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flujomodel',
            name='fecha',
            field=models.CharField(default='', max_length=50),
        ),
    ]