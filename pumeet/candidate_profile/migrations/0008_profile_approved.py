# Generated by Django 3.2.13 on 2022-12-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate_profile', '0007_profile_all_india_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
