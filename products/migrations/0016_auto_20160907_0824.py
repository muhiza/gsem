# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20160907_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='images',
        ),
    ]
