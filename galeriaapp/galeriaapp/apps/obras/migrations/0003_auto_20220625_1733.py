# Generated by Django 3.2.5 on 2022-06-25 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20220625_1733'),
        ('tipo', '0002_auto_20220624_0002'),
        ('obras', '0002_auto_20220625_1733'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Obras',
        ),
        migrations.AddField(
            model_name='obra',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo.tipo'),
        ),
    ]