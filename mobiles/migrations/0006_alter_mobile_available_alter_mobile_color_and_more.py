# Generated by Django 4.2.4 on 2023-08-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0005_rename_country_maker_mobile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='available',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], help_text='it is available or not', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='color',
            field=models.CharField(blank=True, help_text='color of this mobile', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='country',
            field=models.CharField(blank=True, help_text='the contry that makes this mobile', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='model',
            field=models.CharField(blank=True, help_text='model of mobile and must be unique', max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='price',
            field=models.IntegerField(blank=True, help_text='price of this model [$]', null=True),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='screen_size',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='size of screen [inch]', max_digits=4, null=True),
        ),
    ]