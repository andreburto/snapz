# Generated by Django 4.0.4 on 2022-05-22 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_tag_slug_alter_tag_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
