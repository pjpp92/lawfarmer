# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'main_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'main', ['Tag'])

        # Adding model 'Post'
        db.create_table(u'main_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Post'])

        # Adding M2M table for field thema on 'Post'
        m2m_table_name = db.shorten_name(u'main_post_thema')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'main.post'], null=False)),
            ('tag', models.ForeignKey(orm[u'main.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'tag_id'])

        # Adding model 'Comment'
        db.create_table(u'main_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Post'])),
            ('data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'main_tag')

        # Deleting model 'Post'
        db.delete_table(u'main_post')

        # Removing M2M table for field thema on 'Post'
        db.delete_table(db.shorten_name(u'main_post_thema'))

        # Deleting model 'Comment'
        db.delete_table(u'main_comment')


    models = {
        u'main.comment': {
            'Meta': {'object_name': 'Comment'},
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Post']"})
        },
        u'main.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'thema': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.Tag']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'main.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['main']