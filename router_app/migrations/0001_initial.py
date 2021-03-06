# Generated by Django 3.0.7 on 2021-01-30 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RouterDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapId', models.CharField(default=None, max_length=18, unique=True)),
                ('hostName', models.CharField(default=None, max_length=14, null=True)),
                ('loopBack', models.GenericIPAddressField(protocol='IPv4')),
                ('macAdd', models.CharField(default=None, max_length=17, null=True)),
            ],
        ),
    ]
