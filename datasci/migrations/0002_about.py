# Generated by Django 3.2.1 on 2021-05-11 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blurb', models.TextField()),
                ('pic', models.FileField(upload_to='')),
            ],
        ),
    ]