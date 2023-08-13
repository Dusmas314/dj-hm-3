# Generated by Django 4.2.4 on 2023-08-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("image", models.URLField()),
                ("release_date", models.DateField()),
                ("lte_exists", models.BooleanField()),
                ("slug", models.SlugField(max_length=200)),
            ],
        ),
    ]