# Generated by Django 5.0.3 on 2024-03-26 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent_dashboard', '0005_property_property_image'),
        ('user_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent_dashboard.property')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_dashboard.userprofile')),
            ],
            options={
                'unique_together': {('user_profile', 'property')},
            },
        ),
    ]
