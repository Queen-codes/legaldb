# Generated by Django 4.2.16 on 2024-11-01 15:09

# Third-party
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("legal_db", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="is_pending",
            field=models.BooleanField(
                blank=True,
                help_text="Indicate if it is an ongoing case or not.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="case",
            name="license",
            field=models.CharField(
                blank=True,
                help_text="The Creative Commons license associated with the"
                " legal resource.",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="scholarship",
            name="license",
            field=models.CharField(
                blank=True,
                help_text="The Creative Commons license associated with the"
                " legal resource.",
                max_length=50,
                null=True,
            ),
        ),
    ]