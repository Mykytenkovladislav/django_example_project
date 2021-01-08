# Generated by Django 3.1.4 on 2021-01-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20210103_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoredRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=2048, verbose_name='path')),
                ('method', models.CharField(max_length=10, verbose_name='method')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
            ],
        ),
    ]
