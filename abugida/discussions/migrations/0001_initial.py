# Generated by Django 4.0.4 on 2022-05-12 16:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussions.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('body', models.TextField()),
                ('body_image', models.ImageField(blank=True, null=True, upload_to='questions/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('querier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussions.room')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussions.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussions.question')),
                ('responder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussions.room')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussions.topic')),
            ],
        ),
    ]