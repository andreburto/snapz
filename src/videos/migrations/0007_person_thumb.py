# Generated by Django 4.0.4 on 2022-05-08 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_rename_file_name_image_filename_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='thumb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='videos.thumb'),
        ),
    ]