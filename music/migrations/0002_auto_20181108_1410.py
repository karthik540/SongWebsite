# Generated by Django 2.1.1 on 2018-11-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='nos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='time',
            field=models.IntegerField(),
        ),
    ]