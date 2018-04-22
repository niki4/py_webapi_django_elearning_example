from rest_framework import serializers
from . import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('id', 'title')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'user', 'title', 'description',
                  'start_date', 'duration', 'tags', 'webinars')


class WebinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Webinar
        fields = ('id', 'title', 'description', 'scheduled_time')
