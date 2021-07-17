# Generated by Django 3.1.12 on 2021-07-17 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityAPI', '0007_auto_20210717_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(default=None, max_length=100, null=True, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='post',
            name='replyToComment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_reply_to_comment', to='CommunityAPI.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='replyToId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_reply_to_id', to='CommunityAPI.post'),
        ),
    ]
