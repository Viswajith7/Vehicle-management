# Generated by Django 3.2.10 on 2023-08-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=40, null=True)),
                ('Email', models.EmailField(blank=True, max_length=200, null=True)),
                ('Password', models.CharField(blank=True, max_length=40, null=True)),
                ('C_Password', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]
