# Generated by Django 2.1.3 on 2019-02-18 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthAPI', '0010_cssacommitteprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cssacommitteprofile',
            name='role',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UserAuthAPI.CSSARole'),
        ),
    ]
