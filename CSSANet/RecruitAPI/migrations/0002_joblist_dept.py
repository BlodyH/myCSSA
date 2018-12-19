# Generated by Django 2.1.3 on 2018-12-02 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RecruitAPI', '0001_initial'),
        ('UserAuthAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAuthAPI.CSSADept', verbose_name='部门'),
        ),
    ]
