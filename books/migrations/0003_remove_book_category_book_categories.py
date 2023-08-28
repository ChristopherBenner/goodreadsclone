# Generated by Django 4.2.4 on 2023-08-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="category",
        ),
        migrations.AddField(
            model_name="book",
            name="categories",
            field=models.ManyToManyField(related_name="books", to="books.category"),
        ),
    ]
