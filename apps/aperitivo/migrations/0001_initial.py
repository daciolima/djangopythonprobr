# Generated by Django 3.1.2 on 2020-10-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('titulo', models.CharField(max_length=30, unique=True)),
                ('youtube_id', models.CharField(max_length=20, unique=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
