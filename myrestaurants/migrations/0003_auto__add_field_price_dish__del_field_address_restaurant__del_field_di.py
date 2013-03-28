# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Price.dish'
        db.add_column(u'myrestaurants_price', 'dish',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myrestaurants.Dish'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Address.restaurant'
        db.delete_column(u'myrestaurants_address', 'restaurant_id')

        # Deleting field 'Dish.price'
        db.delete_column(u'myrestaurants_dish', 'price_id')

        # Adding field 'Dish.restaurant'
        db.add_column(u'myrestaurants_dish', 'restaurant',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myrestaurants.Restaurant'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Restaurant.dish'
        db.delete_column(u'myrestaurants_restaurant', 'dish_id')

        # Adding field 'Restaurant.address'
        db.add_column(u'myrestaurants_restaurant', 'address',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myrestaurants.Address'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Price.dish'
        db.delete_column(u'myrestaurants_price', 'dish_id')

        # Adding field 'Address.restaurant'
        db.add_column(u'myrestaurants_address', 'restaurant',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myrestaurants.Restaurant'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Dish.price'
        db.add_column(u'myrestaurants_dish', 'price',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myrestaurants.Price'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Dish.restaurant'
        db.delete_column(u'myrestaurants_dish', 'restaurant_id')

        # Adding field 'Restaurant.dish'
        db.add_column(u'myrestaurants_restaurant', 'dish',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myrestaurants.Dish'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Restaurant.address'
        db.delete_column(u'myrestaurants_restaurant', 'address_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'myrestaurants.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'stateOrProvince': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'zipCode': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        u'myrestaurants.dish': {
            'Meta': {'object_name': 'Dish'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myrestaurants.Restaurant']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'myrestaurants.price': {
            'Meta': {'object_name': 'Price'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'currency': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True'}),
            'dish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myrestaurants.Dish']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'myrestaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myrestaurants.Address']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'telephone': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        }
    }

    complete_apps = ['myrestaurants']