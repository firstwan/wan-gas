# Generated by Django 4.0 on 2022-01-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type_name',
            field=models.CharField(choices=[(1, 'Order')], default=1, max_length=50),
        ),
    ]
