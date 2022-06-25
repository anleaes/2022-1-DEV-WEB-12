# Generated by Django 3.2.5 on 2022-06-25 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0002_auto_20220625_1733'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(blank=True, through='orders.OrderItem', to='obras.Obra'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.obra'),
        ),
    ]