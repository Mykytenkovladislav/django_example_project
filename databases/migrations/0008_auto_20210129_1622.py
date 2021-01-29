# Generated by Django 3.1.5 on 2021-01-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0007_auto_20210127_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='quote',
            field=models.TextField(max_length=1000, verbose_name='quote'),
        ),
        migrations.AlterField(
            model_name='quotesauthor',
            name='date_of_birth',
            field=models.CharField(max_length=100, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='quotesauthor',
            name='description',
            field=models.TextField(max_length=6000, verbose_name='description'),
        ),
    ]