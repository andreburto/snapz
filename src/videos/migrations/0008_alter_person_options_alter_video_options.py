# Generated by Django 4.0.4 on 2022-05-12 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_person_thumb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['title', 'filename']},
        ),
    ]
