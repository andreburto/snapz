# Generated by Django 4.0.4 on 2022-05-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_studio_studioname_studionamestudio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studionamestudio',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]
