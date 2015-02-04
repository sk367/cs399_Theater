# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='cost',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
