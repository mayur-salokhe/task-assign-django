# Generated by Django 4.2.4 on 2023-09-05 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_rename_assigned_to_task_assigned_to_group_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assigned_to_user',
            new_name='assigned_by',
        ),
    ]
