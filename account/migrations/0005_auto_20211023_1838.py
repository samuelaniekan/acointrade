# Generated by Django 3.2.8 on 2021-10-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20211023_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='uri',
            field=models.CharField(blank=True, default='3E5FD9DF63', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='wallet_id',
            field=models.CharField(default='585DFA365C', max_length=50, unique=True),
        ),
    ]
