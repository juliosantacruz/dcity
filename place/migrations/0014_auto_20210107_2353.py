# Generated by Django 3.1.4 on 2021-01-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0013_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='phone_owner',
            field=models.IntegerField(verbose_name='telefono del responsable'),
        ),
    ]
