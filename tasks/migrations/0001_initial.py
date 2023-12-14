# Generated by Django 4.2.6 on 2023-12-05 10:09

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
            name='Equipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(db_column='Nome', unique=True)),
                ('sigla', models.TextField(db_column='Sigla', unique=True)),
                ('cidade', models.TextField(blank=True, db_column='Cidade', null=True)),
                ('estado', models.TextField(blank=True, db_column='Estado', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id_estadio', models.AutoField(primary_key=True, serialize=False)),
                ('nome_estadio', models.TextField(unique=True)),
                ('pais', models.TextField(db_column='Pais')),
                ('estado', models.TextField()),
                ('cidade', models.TextField()),
                ('capacidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id_tecnico', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('nacionalidade', models.TextField()),
                ('naturalidade', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_medicamento', models.DateField()),
                ('horario_medicamento', models.TimeField()),
                ('nome_medicamento', models.CharField(max_length=255)),
                ('intervalo_medicamento', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_meal', models.DateField()),
                ('horario_meal', models.TimeField()),
                ('refeicao_meal', models.CharField(max_length=20)),
                ('quantidade_meal', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Glicose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugar_level_glicose', models.IntegerField()),
                ('data_glicose', models.DateField()),
                ('horario_glicose', models.TimeField()),
                ('refeicao_glicose', models.CharField(max_length=20)),
                ('antes_depois_refeicao_glicose', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AtividadeFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_atividade', models.DateField()),
                ('horario_atividade', models.TimeField()),
                ('tipo_atividade', models.CharField(max_length=255)),
                ('duracao_atividade', models.IntegerField()),
                ('intensidade_atividade', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]