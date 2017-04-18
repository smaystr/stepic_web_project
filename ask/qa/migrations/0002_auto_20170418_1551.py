# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(related_name='question_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='question_like_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
