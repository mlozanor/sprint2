# Generated by Django 3.2.6 on 2024-03-16 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BancoDeLosAlpes', '0001_initial'),
        ('Solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('cupo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BancoDeLosAlpes.bancodelosalpes')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Solicitudes.solicitudes')),
            ],
        ),
    ]
