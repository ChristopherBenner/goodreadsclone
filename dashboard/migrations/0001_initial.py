# Generated by Django 4.2.4 on 2023-09-05 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Badge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("points_required", models.IntegerField(default=0)),
                (
                    "awarded_image",
                    models.ImageField(blank=True, null=True, upload_to="badge_images/"),
                ),
                (
                    "not_awarded_image",
                    models.ImageField(blank=True, null=True, upload_to="badge_images/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BadgeCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "Badge Categories",
            },
        ),
        migrations.CreateModel(
            name="Dashboard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "badges",
                    models.ManyToManyField(related_name="badges", to="dashboard.badge"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dashboard",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="badge",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category",
                to="dashboard.badgecategory",
            ),
        ),
    ]
