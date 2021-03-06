# Generated by Django 4.0.4 on 2022-05-16 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_alter_studionamestudio_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='studio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='videos.studio'),
        ),
    ]
