# Generated by Django 3.2.8 on 2021-10-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_transaction_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='pop',
            name='pop',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
