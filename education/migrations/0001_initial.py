# Generated by Django 3.1.1 on 2021-04-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('preferred_study_time', models.CharField(max_length=20)),
                ('study_style', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
            ],
        ),
    ]
