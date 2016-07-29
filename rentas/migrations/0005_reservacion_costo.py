# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentas', '0004_auto_20160626_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='costo',
            field=models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=7),
        ),
    ]
