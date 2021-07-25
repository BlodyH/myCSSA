# Generated by Django 3.1.12 on 2021-07-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityAPI', '0011_auto_20210724_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('user_id', models.UUIDField(primary_key=True, serialize=False, verbose_name='用户的id')),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('avatarUrl', models.URLField(verbose_name='用户头像的url')),
            ],
        ),
    ]
