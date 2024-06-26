# Generated by Django 4.2.7 on 2024-04-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_delete_usermodel_remove_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'pending'), ('done', 'done')], default='pending', max_length=50),
        ),
    ]
