# Generated by Django 2.2.7 on 2019-12-13 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0002_eventday_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventday',
            name='create_by',
        ),
        migrations.RemoveField(
            model_name='eventday',
            name='update_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='create_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='update_by',
        ),
        migrations.AddField(
            model_name='eventday',
            name='create_user',
            field=models.SlugField(default=None),
        ),
        migrations.AddField(
            model_name='eventday',
            name='updated_user',
            field=models.SlugField(default=None),
        ),
        migrations.AddField(
            model_name='user',
            name='create_user',
            field=models.SlugField(default=None),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_user',
            field=models.SlugField(default=None),
        ),
        migrations.AlterField(
            model_name='eventday',
            name='is_delete',
            field=models.IntegerField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_delete',
            field=models.IntegerField(default='0', max_length=1),
        ),
    ]