# Generated by Django 4.2 on 2023-05-29 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Accounts", "0002_account_delete_therapist"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Account",
        ),
    ]
