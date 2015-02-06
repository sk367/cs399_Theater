# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(default=b'', max_length=100)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
