# Generated by Django 2.2.2 on 2019-06-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermgt', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(default='notfound', upload_to='media/photo/%Y/%m/%d'),
        ),
    ]