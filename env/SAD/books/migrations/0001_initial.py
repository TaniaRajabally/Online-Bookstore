
# Generated by Django 2.2.4 on 2019-08-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('book_no', models.BigIntegerField(max_length=100)),
                ('book_url', models.URLField(max_length=250)),
                ('book_genre', models.CharField(max_length=250)),
                ('rating_1', models.BigIntegerField(max_length=100)),
                ('rating_2', models.BigIntegerField(max_length=100)),
                ('rating_3', models.BigIntegerField(max_length=100)),
                ('rating_4', models.BigIntegerField(max_length=100)),
                ('rating_count', models.BigIntegerField(max_length=100)),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.BigIntegerField(max_length=100)),
            ],
        ),
    ]
