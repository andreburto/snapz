# Generated by Django 4.0.4 on 2022-05-15 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkz', '0001_initial'),
        ('videos', '0009_linkpeople'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudioName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudioNameStudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.BooleanField()),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='videos.studio')),
                ('studio_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='videos.studioname')),
            ],
        ),
        migrations.AddField(
            model_name='studio',
            name='studio_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='videos.studioname'),
        ),
        migrations.AddField(
            model_name='studio',
            name='website',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='linkz.link'),
        ),
    ]