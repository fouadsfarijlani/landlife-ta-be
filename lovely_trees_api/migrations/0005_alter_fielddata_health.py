# Generated by Django 4.1.3 on 2022-11-14 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lovely_trees_api', '0004_alter_fielddata_health'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fielddata',
            name='health',
            field=models.IntegerField(blank=True, choices=[(0, 'Unkown'), (1, 'Poor'), (2, 'Ok'), (3, 'Excellent')], null=True),
        ),
    ]
