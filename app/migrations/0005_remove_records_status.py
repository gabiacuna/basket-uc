# Generated by Django 5.1.2 on 2024-10-28 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_records_delete_validation_remove_user_id_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='status',
        ),
    ]
