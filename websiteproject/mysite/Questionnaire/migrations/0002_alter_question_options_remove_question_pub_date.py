# Generated by Django 4.2 on 2023-05-31 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Questionnaire", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="question",
            options={"ordering": ["text"]},
        ),
        migrations.RemoveField(
            model_name="question",
            name="pub_date",
        ),
    ]
