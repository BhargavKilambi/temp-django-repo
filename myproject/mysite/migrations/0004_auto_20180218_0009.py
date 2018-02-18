# Generated by Django 2.0.2 on 2018-02-17 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_site_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]