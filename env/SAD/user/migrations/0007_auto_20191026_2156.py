# Generated by Django 2.2.4 on 2019-10-26 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0006_order_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='book_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.Books'),
        ),
    ]
