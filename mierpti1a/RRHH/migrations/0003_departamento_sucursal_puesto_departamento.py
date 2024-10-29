# Generated by Django 4.2.16 on 2024-10-07 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("RRHH", "0002_departamento_puesto_sucursal_empleado_foto_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="departamento",
            name="sucursal",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departamentos",
                to="RRHH.sucursal",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="puesto",
            name="departamento",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="puestos",
                to="RRHH.departamento",
            ),
            preserve_default=False,
        ),
    ]
