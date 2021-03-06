# Generated by Django 2.0.3 on 2018-08-01 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Select a genre for this book', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Genre'),
        ),
    ]
