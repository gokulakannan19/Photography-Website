# Generated by Django 2.2.15 on 2020-11-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bride_name', models.CharField(max_length=30)),
                ('groom_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('phone', models.IntegerField(max_length=10)),
                ('referrals', models.TextField(max_length=200)),
            ],
        ),
    ]
