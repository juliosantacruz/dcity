# Generated by Django 3.1.4 on 2020-12-16 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_auto_20201215_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicemenu',
            old_name='fs_category',
            new_name='product_category',
        ),
        migrations.RenameField(
            model_name='servicemenu',
            old_name='fs_description',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='servicemenu',
            old_name='fs_image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='servicemenu',
            old_name='fs_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='servicemenu',
            old_name='fs_orden',
            new_name='product_orden',
        ),
        migrations.RenameField(
            model_name='servicemenu',
            old_name='fs_price',
            new_name='product_price',
        ),
    ]
