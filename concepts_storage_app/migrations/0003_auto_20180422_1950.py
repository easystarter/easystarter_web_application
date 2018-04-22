# Generated by Django 2.0.3 on 2018-04-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts_storage_app', '0002_concept_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='day_to_go',
            field=models.CharField(choices=[(30, '30 days to go, platform fee is 5% of the project cost'), (45, '45 days to go, platform fee is 10% of the project cost'), (60, '60 days to go, platform fee is 15% of the project cost')], default=30, max_length=100),
        ),
    ]
