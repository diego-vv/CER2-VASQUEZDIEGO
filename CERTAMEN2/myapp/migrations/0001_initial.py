# Generated by Django 4.2.6 on 2023-10-24 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Comunicado',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('detalle', models.CharField(max_length=255)),
                ('detalle_corto', models.CharField(max_length=160)),
                ('tipo', models.CharField(choices=[('S', 'suspencion de actividades'), ('C', 'Suspencion de clase'), ('I', 'Informacion')], max_length=1)),
                ('visible', models.BooleanField()),
                ('fecha_publicacion', models.DateTimeField()),
                ('fecha_ultima_publicacion', models.DateTimeField()),
                ('entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.entidad')),
                ('modificado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunicados_modificados', to=settings.AUTH_USER_MODEL)),
                ('publicado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunicados_publicados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]