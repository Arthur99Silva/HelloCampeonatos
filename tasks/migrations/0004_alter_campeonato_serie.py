# Generated by Django 4.2.6 on 2023-12-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_campeonato_remove_estadio_id_estadio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeonato',
            name='serie',
            field=models.CharField(max_length=1),
        ),
    ]
