# Generated by Django 3.1.5 on 2021-01-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0016_auto_20210114_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cupon',
            name='cupon_used',
        ),
        migrations.AddField(
            model_name='servicemenu',
            name='product_category_detail',
            field=models.TextField(blank=True, null=True, verbose_name='Detalles de categoria'),
        ),
    ]