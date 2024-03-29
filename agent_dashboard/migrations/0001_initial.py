# Generated by Django 5.0.3 on 2024-03-18 15:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(editable=False, max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('type', models.CharField(choices=[('House', 'House'), ('Plot', 'Plot'), ('Business Building', 'Business Building')], max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('seller_name', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=10)),
                ('bedrooms', models.IntegerField(default=0)),
                ('bathrooms', models.IntegerField(default=0)),
                ('kitchens', models.IntegerField(default=0)),
                ('floor', models.IntegerField(default=0)),
                ('area', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('govt_id', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=100)),
                ('agent_id', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
