# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-16 17:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microsite_configuration', '0003_delete_historical_records'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='microsite',
            name='site',
        ),
        migrations.RemoveField(
            model_name='micrositehistory',
            name='site',
        ),
        migrations.RemoveField(
            model_name='micrositeorganizationmapping',
            name='microsite',
        ),
        migrations.AlterUniqueTogether(
            name='micrositetemplate',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='micrositetemplate',
            name='microsite',
        ),
        migrations.DeleteModel(
            name='Microsite',
        ),
        migrations.DeleteModel(
            name='MicrositeHistory',
        ),
        migrations.DeleteModel(
            name='MicrositeOrganizationMapping',
        ),
        migrations.DeleteModel(
            name='MicrositeTemplate',
        ),
    ]
