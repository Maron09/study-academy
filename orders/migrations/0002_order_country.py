# Generated by Django 5.0.7 on 2024-08-08 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]