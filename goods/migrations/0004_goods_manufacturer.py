# Generated by Django 4.2 on 2023-05-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goods", "0003_goods_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="goods",
            name="manufacturer",
            field=models.CharField(default="", max_length=500),
        ),
    ]
