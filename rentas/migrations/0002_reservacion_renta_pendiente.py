# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='renta_pendiente',
            field=models.BooleanField(default='ca'),
            preserve_default=False,
        ),
    ]
