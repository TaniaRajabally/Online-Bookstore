# Generated by Django 2.2.4 on 2019-08-13 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_no',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating_1',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating_2',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating_3',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating_4',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating_count',
            field=models.IntegerField(max_length=100),
        ),
    ]
