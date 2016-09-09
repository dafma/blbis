# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0005_reservacion_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='renta_pendiente',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reservacion',
            name='tyc',
            field=models.BooleanField(verbose_name='Terminos y condiciones', default=False),
        ),
    ]
