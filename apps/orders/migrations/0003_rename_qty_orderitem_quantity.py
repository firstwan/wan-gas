# Generated by Django 4.0 on 2022-01-02 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qty',
            new_name='quantity',
        ),
    ]
