# Generated by Django 2.2.15 on 2020-11-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photosite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
