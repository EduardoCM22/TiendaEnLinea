# Generated by Django 5.1.1 on 2024-10-06 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecar", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="carritoproducto",
            unique_together={("carrito", "producto")},
        ),
    ]
