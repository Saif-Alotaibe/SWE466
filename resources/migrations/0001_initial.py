# Generated by Django 3.1.7 on 2021-03-20 12:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date updated')),
                ('name', models.CharField(max_length=70)),
                ('resource_type', models.CharField(max_length=70)),
                ('material', models.CharField(max_length=70)),
                ('max_number_of_resources', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
