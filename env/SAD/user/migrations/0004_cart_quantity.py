# Generated by Django 2.2.4 on 2019-10-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
