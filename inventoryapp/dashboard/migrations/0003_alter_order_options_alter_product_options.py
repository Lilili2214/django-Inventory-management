# Generated by Django 5.0.6 on 2024-06-07 09:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_order"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name_plural": "Order"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name_plural": "Product"},
        ),
    ]
