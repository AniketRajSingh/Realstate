# Generated by Django 5.0.3 on 2024-03-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent_dashboard', '0004_agentprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_image',
            field=models.ImageField(blank=True, null=True, upload_to='Properties/'),
        ),
    ]
