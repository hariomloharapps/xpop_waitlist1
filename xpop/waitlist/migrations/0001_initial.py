# Generated by Django 5.2.1 on 2025-06-04 08:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaitlistUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="User's full name", max_length=100)),
                ('email', models.EmailField(help_text="User's email address (must be unique)", max_length=254, unique=True)),
                ('agree_to_help', models.BooleanField(default=False, help_text='Whether user agreed to help with beta testing')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='When the user joined the waitlist')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last time the record was updated')),
            ],
            options={
                'verbose_name': 'Waitlist User',
                'verbose_name_plural': 'Waitlist Users',
                'ordering': ['-created_at'],
            },
        ),
    ]
