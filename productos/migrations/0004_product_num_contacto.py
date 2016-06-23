# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20160519_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='num_contacto',
            field=models.CharField(default='1234567890', max_length=14),
        ),
    ]
