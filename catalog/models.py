from django.db import models
from otus_site import settings


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Course(models.Model):
    user = models.ForeignKey(
        settings.Base.AUTH_USER_MODEL,
        related_name='courses',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.DurationField()

    tags = models.ManyToManyField('Tag', blank=True)
    webinars = models.ManyToManyField('Webinar', blank=True)

    def __str__(self):
        return self.title


class Webinar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.title
