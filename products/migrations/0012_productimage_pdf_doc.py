# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20160830_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='pdf_doc',
            field=models.FileField(default=b'', upload_to=products.models.image_upload_to),
        ),
    ]
