# Generated by Django 4.2.4 on 2023-08-06 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0004_rename_brand_name_mobile_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='country_maker',
            new_name='country',
        ),
    ]