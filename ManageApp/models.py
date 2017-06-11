# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from rest_framework import routers, serializers, viewsets
from django.db import models


# Create your models here.
class TestMmodel(models.Model):

    us_name = models.CharField(u'名字', max_length=10)
    age = models.IntegerField()
    of_on = models.BooleanField()

    class Meta:
        db_table = "us_table"

    def __unicode__(self):
        return self.us_name


class UserAdmin(admin.ModelAdmin):
    list_display = ('us_name', 'age', 'of_on')
    list_display_links = ('us_name',)
    list_select_related = True
    list_editable = ('age', 'of_on')
    search_fields = ('age', 'us_name')
    list_filter = ('age', 'us_name')
    actions = ['test_action', ]

    def test_action(self, request, queryset):
        queryset.update(of_on=0)
        self.message_user(request, 'successful')

    test_action.short_description = mark_safe('test')


class TestModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestMmodel
        fields = ('url', 'us_name', 'age')


class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TestMmodel.objects.all()
    serializer_class = TestModelSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'test_model', TestModelViewSet)
admin.site.register(TestMmodel, UserAdmin)
