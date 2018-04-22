from django.shortcuts import render

from rest_framework import viewsets
from otus_site import permissions

from . import models, serializers


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [permissions.IsAccountAdminOrReadOnly, ]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [permissions.IsAccountAdminOrReadOnly, ]


class WebinarViewSet(viewsets.ModelViewSet):
    queryset = models.Webinar.objects.all()
    serializer_class = serializers.WebinarSerializer
    permission_classes = [permissions.IsAccountAdminOrReadOnly, ]
