# Generated by Django 3.0.4 on 2020-05-04 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_auto_20200503_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialist', to=settings.AUTH_USER_MODEL),
        ),
    ]