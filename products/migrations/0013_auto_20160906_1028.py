# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_productimage_pdf_doc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='pdf_doc',
            new_name='documents',
        ),
    ]
