# Generated by Django 2.1.7 on 2019-03-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20190329_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]