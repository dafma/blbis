# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0003_reservacion_tyc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacion',
            name='tyc',
            field=models.BooleanField(verbose_name='Terminos y condiciones'),
        ),
    ]
