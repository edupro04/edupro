# Generated by Django 4.2.10 on 2024-03-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAccounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
