# Generated by Django 4.0.1 on 2022-02-01 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('base_price_currency', models.CharField(default='MYR', max_length=4)),
                ('base_price', models.DecimalField(decimal_places=4, max_digits=18)),
                ('qty_in_stock', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=250)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_type_id', models.IntegerField(choices=[(1, 'Restock'), (2, 'Sell'), (3, 'Manual Adjust')])),
                ('history_type_name', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('remark', models.CharField(max_length=250)),
                ('created_by', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('action_reference_id', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
            options={
                'db_table': 'product_history',
            },
        ),
    ]
