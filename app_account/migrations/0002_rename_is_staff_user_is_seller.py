# Generated by Django 4.2.8 on 2023-12-24 13:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_account", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_staff",
            new_name="is_seller",
        ),
    ]