# Generated by Django 5.0.7 on 2024-07-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='for_who',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='reason',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
