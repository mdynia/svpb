# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arbeitsplan', '0005_auto_20141128_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitglied',
            name='gender',
            field=models.CharField(default=b'M', max_length=1, verbose_name=b'Geschlecht'),
            preserve_default=True,
        ),
    ]
