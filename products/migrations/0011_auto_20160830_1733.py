# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_productimage_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='doc',
            field=models.FileField(default=b'doc', upload_to=products.models.document_upload_to),
        ),
    ]
