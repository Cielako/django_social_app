# Generated by Django 5.1.2 on 2024-12-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_panel", "0004_alter_profile_gender_alter_profile_orientation"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="first_name",
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name="profile",
            name="gender",
            field=models.IntegerField(
                choices=[(2, "not specified"), (1, "female"), (0, "male")], default=2
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="orientation",
            field=models.IntegerField(
                choices=[
                    (0, "heterosexual"),
                    (1, "homosexual"),
                    (3, "asexual"),
                    (2, "bisexual"),
                ],
                default=0,
            ),
        ),
    ]
