# Generated by Django 4.2.6 on 2023-11-06 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlHardware', '0004_capacidad_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialCompras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCompa', models.DateField(null=True)),
                ('codigo', models.CharField(max_length=60)),
                ('activo', models.BooleanField(default=True)),
                ('actualizacionUsuario', models.IntegerField(blank=True, null=True)),
                ('creacionFechaHora', models.DateTimeField(auto_now_add=True, null=True)),
                ('actualizacionFechaHora', models.DateTimeField(auto_now=True, null=True)),
                ('proveedorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='controlHardware.proveedor')),
            ],
        ),
    ]
