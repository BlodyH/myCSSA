# Generated by Django 2.1.3 on 2019-01-03 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthAPI', '0003_auto_20190103_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useracademic',
            name='userProfile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
