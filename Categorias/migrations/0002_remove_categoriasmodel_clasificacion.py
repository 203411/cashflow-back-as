# Generated by Django 4.0.3 on 2022-03-18 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Categorias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriasmodel',
            name='clasificacion',
        ),
    ]
