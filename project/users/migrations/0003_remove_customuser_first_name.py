# Generated by Django 5.1.2 on 2024-12-29 12:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_customuser_groups_customuser_user_permissions"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="first_name",
        ),
    ]
