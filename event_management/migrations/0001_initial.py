# Generated by Django 2.2.7 on 2020-02-05 03:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventDay',
            fields=[
                ('is_deleted', models.CharField(default='0', max_length=1)),
                ('created_user', models.SlugField(default=None)),
                ('updated_user', models.SlugField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=25)),
                ('date', models.DateField()),
                ('local', models.CharField(default='', max_length=30)),
                ('content', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'event_day',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.CharField(default='0', max_length=1)),
                ('created_user', models.SlugField(default=None)),
                ('updated_user', models.SlugField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('first_name', models.CharField(default='', max_length=20)),
                ('birthday', models.DateField(null=True)),
                ('sex', models.CharField(default='', max_length=6)),
                ('email', models.EmailField(default='', max_length=50)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('is_deleted', models.CharField(default='0', max_length=1)),
                ('created_user', models.SlugField(default=None)),
                ('updated_user', models.SlugField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event_management.EventDay')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='event_management.User')),
            ],
            options={
                'db_table': 'event_user',
            },
        ),
    ]
