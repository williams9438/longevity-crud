from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from api.views import UserViewSet, UsersViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
