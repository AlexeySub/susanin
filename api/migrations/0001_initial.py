# Generated by Django 2.1.7 on 2019-04-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.AutoField(null=None, primary_key=True, serialize=False, unique=True)),
                ('busStopName', models.CharField(max_length=32)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]