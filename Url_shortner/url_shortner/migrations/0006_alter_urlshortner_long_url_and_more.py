# Generated by Django 4.2.7 on 2023-11-01 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("url_shortner", "0005_alter_urlshortner_short_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="urlshortner",
            name="long_url",
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name="urlshortner",
            name="short_url",
            field=models.CharField(max_length=20),
        ),
    ]