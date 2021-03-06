# Generated by Django 3.1.1 on 2021-04-11 02:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='preferred_study_time',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='study_style',
            new_name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='study_period',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='study_time',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='volume',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
