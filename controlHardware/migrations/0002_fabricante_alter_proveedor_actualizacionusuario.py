# Generated by Django 4.2.6 on 2023-11-06 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlHardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('activo', models.BooleanField(default=True)),
                ('actualizacionUsuario', models.IntegerField(blank=True, null=True)),
                ('creacionFechaHora', models.DateTimeField(auto_now_add=True, null=True)),
                ('actualizacionFechaHora', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='actualizacionUsuario',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
