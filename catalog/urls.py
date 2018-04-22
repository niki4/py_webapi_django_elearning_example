from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'webinars', views.WebinarViewSet)

app_name = 'catalog'
urlpatterns = [
    url(r'^', include(router.urls))
]
