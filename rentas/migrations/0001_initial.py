# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0003_auto_20160519_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('cliente', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(to='productos.Product')),
            ],
            options={
                'verbose_name': 'Reservaciones',
                'verbose_name_plural': 'Reservaciones',
            },
        ),
    ]
