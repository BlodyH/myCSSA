# Generated by Django 2.2 on 2019-04-20 01:35

import PhotoCompetition.models
from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('PhotoCompetition', '0002_auto_20190419_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='upload_photo',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=PhotoCompetition.models._GetUserDir, verbose_name='上传作品'),
        ),
    ]
