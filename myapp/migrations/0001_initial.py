# Generated by Django 2.0.7 on 2018-07-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField()),
                ('resume', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.IntegerField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('work_exp', models.CharField(blank=True, max_length=100, null=True)),
                ('current_loc', models.CharField(blank=True, max_length=100, null=True)),
                ('corrected_loc', models.CharField(blank=True, max_length=100, null=True)),
                ('nearest_city', models.CharField(blank=True, max_length=100, null=True)),
                ('preferred_loc', models.CharField(blank=True, max_length=100, null=True)),
                ('ctc', models.FloatField(blank=True, max_length=100, null=True)),
                ('current_employer', models.CharField(blank=True, max_length=100, null=True)),
                ('current_designation', models.CharField(blank=True, max_length=100, null=True)),
                ('skills', models.CharField(blank=True, max_length=255, null=True)),
                ('ug_course', models.CharField(blank=True, max_length=255, null=True)),
                ('ug_institute', models.CharField(blank=True, max_length=255, null=True)),
                ('ug_passing_yr', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
