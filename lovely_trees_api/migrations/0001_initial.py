# Generated by Django 4.1.3 on 2022-11-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldData',
            fields=[
                ('individual_tree_id', models.IntegerField(primary_key=True, serialize=False)),
                ('species_id', models.IntegerField()),
                ('method', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('health', models.IntegerField(choices=[(1, 'Poor'), (2, 'Ok'), (3, 'Excellent'), (4, 'Na')])),
                ('year_monitored', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('tree_species_id', models.IntegerField(primary_key=True, serialize=False)),
                ('latin_name', models.CharField(max_length=100)),
            ],
        ),
    ]
