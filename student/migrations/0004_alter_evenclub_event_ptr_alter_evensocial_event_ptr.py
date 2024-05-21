# Generated by Django 5.0.4 on 2024-04-22 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_evenclub_event_ptr_alter_evensocial_event_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenclub',
            name='event_ptr',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.event'),
        ),
        migrations.AlterField(
            model_name='evensocial',
            name='event_ptr',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.event'),
        ),
    ]
