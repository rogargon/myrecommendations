# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Review'
        db.delete_table(u'myrestaurants_review')

        # Deleting model 'Address'
        db.delete_table(u'myrestaurants_address')

        # Deleting field 'RestaurantReview.review_ptr'
        db.delete_column(u'myrestaurants_restaurantreview', u'review_ptr_id')

        # Adding field 'RestaurantReview.id'
        db.add_column(u'myrestaurants_restaurantreview', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Adding field 'RestaurantReview.rating'
        db.add_column(u'myrestaurants_restaurantreview', 'rating',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3),
                      keep_default=False)

        # Adding field 'RestaurantReview.comment'
        db.add_column(u'myrestaurants_restaurantreview', 'comment',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RestaurantReview.user'
        db.add_column(u'myrestaurants_restaurantreview', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'RestaurantReview.date'
        db.add_column(u'myrestaurants_restaurantreview', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.date.today),
                      keep_default=False)


        # Changing field 'Dish.description'
        db.alter_column(u'myrestaurants_dish', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Dish.restaurant'
        db.alter_column(u'myrestaurants_dish', 'restaurant_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['myrestaurants.Restaurant']))

        # Changing field 'Dish.user'
        db.alter_column(u'myrestaurants_dish', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Dish.date'
        db.alter_column(u'myrestaurants_dish', 'date', self.gf('django.db.models.fields.DateField')())
        # Deleting field 'Restaurant.address'
        db.delete_column(u'myrestaurants_restaurant', 'address_id')

        # Adding field 'Restaurant.street'
        db.add_column(u'myrestaurants_restaurant', 'street',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Restaurant.number'
        db.add_column(u'myrestaurants_restaurant', 'number',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Restaurant.city'
        db.add_column(u'myrestaurants_restaurant', 'city',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Restaurant.zipCode'
        db.add_column(u'myrestaurants_restaurant', 'zipCode',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Restaurant.stateOrProvince'
        db.add_column(u'myrestaurants_restaurant', 'stateOrProvince',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Restaurant.country'
        db.add_column(u'myrestaurants_restaurant', 'country',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Restaurant.url'
        db.alter_column(u'myrestaurants_restaurant', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Restaurant.telephone'
        db.alter_column(u'myrestaurants_restaurant', 'telephone', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Restaurant.user'
        db.alter_column(u'myrestaurants_restaurant', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Restaurant.date'
        db.alter_column(u'myrestaurants_restaurant', 'date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Adding model 'Review'
        db.create_table(u'myrestaurants_review', (
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=3)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today, null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'myrestaurants', ['Review'])

        # Adding model 'Address'
        db.create_table(u'myrestaurants_address', (
            ('city', self.gf('django.db.models.fields.TextField')()),
            ('street', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today, null=True)),
            ('country', self.gf('django.db.models.fields.TextField')()),
            ('stateOrProvince', self.gf('django.db.models.fields.TextField')(blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zipCode', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'myrestaurants', ['Address'])

        # Adding field 'RestaurantReview.review_ptr'
        db.add_column(u'myrestaurants_restaurantreview', u'review_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['myrestaurants.Review'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'RestaurantReview.id'
        db.delete_column(u'myrestaurants_restaurantreview', u'id')

        # Deleting field 'RestaurantReview.rating'
        db.delete_column(u'myrestaurants_restaurantreview', 'rating')

        # Deleting field 'RestaurantReview.comment'
        db.delete_column(u'myrestaurants_restaurantreview', 'comment')

        # Deleting field 'RestaurantReview.user'
        db.delete_column(u'myrestaurants_restaurantreview', 'user_id')

        # Deleting field 'RestaurantReview.date'
        db.delete_column(u'myrestaurants_restaurantreview', 'date')


        # Changing field 'Dish.description'
        db.alter_column(u'myrestaurants_dish', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Dish.restaurant'
        db.alter_column(u'myrestaurants_dish', 'restaurant_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myrestaurants.Restaurant'], null=True))

        # Changing field 'Dish.user'
        db.alter_column(u'myrestaurants_dish', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'Dish.date'
        db.alter_column(u'myrestaurants_dish', 'date', self.gf('django.db.models.fields.DateField')(null=True))
        # Adding field 'Restaurant.address'
        db.add_column(u'myrestaurants_restaurant', 'address',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myrestaurants.Address'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Restaurant.street'
        db.delete_column(u'myrestaurants_restaurant', 'street')

        # Deleting field 'Restaurant.number'
        db.delete_column(u'myrestaurants_restaurant', 'number')

        # Deleting field 'Restaurant.city'
        db.delete_column(u'myrestaurants_restaurant', 'city')

        # Deleting field 'Restaurant.zipCode'
        db.delete_column(u'myrestaurants_restaurant', 'zipCode')

        # Deleting field 'Restaurant.stateOrProvince'
        db.delete_column(u'myrestaurants_restaurant', 'stateOrProvince')

        # Deleting field 'Restaurant.country'
        db.delete_column(u'myrestaurants_restaurant', 'country')


        # Changing field 'Restaurant.url'
        db.alter_column(u'myrestaurants_restaurant', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Restaurant.telephone'
        db.alter_column(u'myrestaurants_restaurant', 'telephone', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Restaurant.user'
        db.alter_column(u'myrestaurants_restaurant', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'Restaurant.date'
        db.alter_column(u'myrestaurants_restaurant', 'date', self.gf('django.db.models.fields.DateField')(null=True))

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
        u'myrestaurants.dish': {
            'Meta': {'object_name': 'Dish'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myrestaurants.Restaurant']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'myrestaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'city': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'stateOrProvince': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'zipCode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'myrestaurants.restaurantreview': {
            'Meta': {'object_name': 'RestaurantReview'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '3'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myrestaurants.Restaurant']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['myrestaurants']