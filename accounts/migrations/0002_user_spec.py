# Generated by Django 3.0.4 on 2020-05-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='spec',
            field=models.BooleanField(default=True),
        ),
    ]