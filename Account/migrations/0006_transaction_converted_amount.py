# Generated by Django 3.2.14 on 2022-08-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_transaction_converted_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='converted_amount',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=15),
        ),
    ]
