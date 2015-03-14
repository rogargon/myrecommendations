# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(null=True, verbose_name=b'Euro amount', max_digits=8, decimal_places=2, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'myrestaurants', blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('street', models.TextField(null=True, blank=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('city', models.TextField(default=b'')),
                ('zipCode', models.TextField(null=True, blank=True)),
                ('stateOrProvince', models.TextField(null=True, blank=True)),
                ('country', models.TextField(null=True, blank=True)),
                ('telephone', models.TextField(null=True, blank=True)),
                ('web', models.URLField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, verbose_name=b'Ratings (stars)', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('comment', models.TextField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('restaurant', models.ForeignKey(to='myrestaurants.Restaurant')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(related_name='dishes', to='myrestaurants.Restaurant', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dish',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
