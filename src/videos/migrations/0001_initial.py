# Generated by Django 4.0.4 on 2022-04-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('base64_filename', models.TextField()),
            ],
        ),
    ]