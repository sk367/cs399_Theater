# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=128)),
                ('date', models.DateTimeField()),
                ('cost', models.DecimalField(max_digits=3, decimal_places=2)),
                ('genre', models.CharField(default=b'folk', max_length=50)),
                ('description', models.TextField(default=b'This band plays music')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
