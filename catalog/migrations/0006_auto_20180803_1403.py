# Generated by Django 2.0.3 on 2018-08-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180803_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death',
            field=models.DateField(blank=True, null=True, verbose_name='Died'),
        ),
    ]
