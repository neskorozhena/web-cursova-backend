# Generated by Django 4.2 on 2023-05-01 10:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order_status", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="orderstatus",
            options={"verbose_name_plural": "Order Statuses"},
        ),
    ]
