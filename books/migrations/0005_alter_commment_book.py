# Generated by Django 4.2.4 on 2023-08-29 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_commment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commment",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="books.book",
            ),
        ),
    ]
