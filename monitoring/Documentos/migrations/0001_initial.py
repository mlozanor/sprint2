# Generated by Django 3.2.6 on 2024-03-16 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0001_initial'),
        ('Solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.clientes')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Solicitudes.solicitudes')),
            ],
        ),
    ]
