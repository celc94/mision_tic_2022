# Generated by Django 4.1 on 2022-09-01 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Lineas_De_Credito',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('plazomax', models.IntegerField()),
                ('montomax', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('codigo_credito', models.IntegerField(primary_key=True, serialize=False)),
                ('monto_prestado', models.IntegerField()),
                ('fecha_credito', models.DateField()),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcooperativa.lineas_de_credito')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcooperativa.cliente')),
            ],
        ),
    ]
