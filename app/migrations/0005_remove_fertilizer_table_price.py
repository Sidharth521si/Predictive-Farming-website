# Generated by Django 3.2.25 on 2024-12-25 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_table_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizer_table',
            name='price',
        ),
    ]
