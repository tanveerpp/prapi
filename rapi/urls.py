from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from home.StudentViewset import StudentViewSet
router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
