# Generated by Django 2.1.7 on 2019-03-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCSSAhub', '0018_auto_20190313_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountmerchant',
            name='merchant_qrcode',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/usrImage/merchantWechatQRcode', verbose_name='微信二维码'),
        ),
    ]
