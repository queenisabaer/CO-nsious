# Generated by Django 4.2.16 on 2024-11-28 10:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeProfile",
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
                    "total_points",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "employee_image",
                    django_resized.forms.ResizedImageField(
                        crop=None,
                        default="/profiles/profile_footprint_jowwx7.png",
                        force_format="WEBP",
                        keep_meta=True,
                        quality=100,
                        scale=None,
                        size=[200, None],
                        upload_to="profiles/",
                    ),
                ),
                (
                    "image_alt",
                    models.CharField(default="profile image", max_length=100),
                ),
                (
                    "employee",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
