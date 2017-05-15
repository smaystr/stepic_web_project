# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20170418_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('added_at',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-added_at',)},
        ),
    ]
