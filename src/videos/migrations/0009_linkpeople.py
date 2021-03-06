# Generated by Django 4.0.4 on 2022-05-12 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkz', '0001_initial'),
        ('videos', '0008_alter_person_options_alter_video_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='linkz.link')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='videos.person')),
            ],
        ),
    ]
