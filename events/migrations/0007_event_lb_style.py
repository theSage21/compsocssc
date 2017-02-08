# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20170204_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lb_style',
            field=models.CharField(default=b'ggplot', help_text=b'The style in which the LB is plotted if it is plotted at all.\n            Refer to https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html\n            for guidance ', max_length=50, choices=[(b'bmh', b'bmh'), (b'classic', b'classic'), (b'dark_background', b'dark_background'), (b'fivethirtyeight', b'fivethirtyeight'), (b'ggplot', b'ggplot'), (b'grayscale', b'grayscale'), (b'seaborn-bright', b'seaborn-bright'), (b'seaborn-colorblind', b'seaborn-colorblind'), (b'seaborn-dark', b'seaborn-dark'), (b'seaborn-dark-palletteseaborn-darkgrid', b'seaborn-dark-palletteseaborn-darkgrid'), (b'seaborn-deep', b'seaborn-deep'), (b'seaborn-muted', b'seaborn-muted'), (b'seaborn-notebook', b'seaborn-notebook'), (b'seaborn-pastel', b'seaborn-pastel'), (b'seaborn-poster', b'seaborn-poster'), (b'seaborn-talk', b'seaborn-talk'), (b'seaborn-ticks', b'seaborn-ticks'), (b'seaborn-white', b'seaborn-white'), (b'seaborn-whitegrid', b'seaborn-whitegrid')]),
        ),
    ]
