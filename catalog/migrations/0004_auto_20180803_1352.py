# Generated by Django 2.0.3 on 2018-08-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180803_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateField(blank=True, help_text='Enter the year of publication', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.DateField(blank=True, help_text='Enter the year of publication', null=True),
        ),
    ]
