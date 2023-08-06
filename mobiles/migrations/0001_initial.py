# Generated by Django 4.2.4 on 2023-08-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(help_text='brand name of mobile', max_length=32)),
                ('nationality', models.CharField(help_text='main country that investigate this mobile', max_length=64)),
                ('model', models.CharField(help_text='model of mobile and must be unique', max_length=128, unique=True)),
                ('price', models.IntegerField(help_text='price of this model [$]')),
                ('color', models.CharField(help_text='color of this mobile', max_length=64)),
                ('screen_size', models.IntegerField(help_text='size of screen [inch]')),
                ('available', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], help_text='it is available or not', max_length=1)),
                ('country_maker', models.CharField(help_text='the contry that makes this mobile', max_length=64)),
                ('insert_time', models.DateTimeField(auto_now_add=True, help_text='time of saving this row to database')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='time of last update of this row')),
            ],
        ),
    ]
