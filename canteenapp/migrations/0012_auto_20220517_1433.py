# Generated by Django 2.0.2 on 2022-05-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteenapp', '0011_auto_20220513_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill5',
            fields=[
                ('key', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('price', models.CharField(max_length=60)),
                ('item', models.CharField(max_length=60)),
                ('quan', models.CharField(max_length=60)),
                ('ids', models.CharField(max_length=60)),
                ('time', models.CharField(max_length=60)),
                ('date', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=60)),
                ('qprice', models.CharField(max_length=60)),
                ('use', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='bill4',
        ),
    ]
