# Generated by Django 5.1.1 on 2024-09-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="is_readonly",
            field=models.BooleanField(default=False),
        ),
    ]
