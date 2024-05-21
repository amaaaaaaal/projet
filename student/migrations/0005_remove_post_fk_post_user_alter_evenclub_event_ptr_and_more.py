# Generated by Django 5.0.4 on 2024-04-22 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_evenclub_event_ptr_alter_evensocial_event_ptr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='fk',
        ),
        migrations.AddField(
            model_name='post',
            name='User',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='student.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evenclub',
            name='event_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.event'),
        ),
        migrations.AlterField(
            model_name='evensocial',
            name='event_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.event'),
        ),
    ]