# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0002_reservacion_renta_pendiente'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='tyc',
            field=models.BooleanField(default=False),
        ),
    ]
