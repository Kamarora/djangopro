# Generated by Django 2.0.7 on 2018-07-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
