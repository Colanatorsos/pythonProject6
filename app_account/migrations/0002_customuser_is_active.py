# Generated by Django 4.2.8 on 2023-12-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]