# Generated by Django 5.0.4 on 2024-05-01 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='organizador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos_organizados', to='eventos.usuario'),
        ),
    ]
