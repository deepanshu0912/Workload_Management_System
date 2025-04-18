# Generated by Django 5.1.1 on 2025-04-05 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Food', '0001_initial'),
        ('User', '0002_rename_mobile_usercredentials_userid_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('order_channel', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('New', 'New'), ('Preparing', 'Preparing'), ('Completed', 'Completed')], max_length=255)),
                ('timestamp', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Order_Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number_of_items', models.IntegerField()),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Processing', 'Processing'), ('Pending', 'Pending')], max_length=255)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Food.food_items')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.orders')),
            ],
            options={
                'verbose_name': 'Order_Item',
                'verbose_name_plural': 'Order_Items',
            },
        ),
    ]
