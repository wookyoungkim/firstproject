# Generated by Django 2.2.3 on 2019-07-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
