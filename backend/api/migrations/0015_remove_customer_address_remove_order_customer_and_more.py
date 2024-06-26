# Generated by Django 4.2.7 on 2024-04-10 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_order_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.cart'),
            preserve_default=False,
        ),
    ]
