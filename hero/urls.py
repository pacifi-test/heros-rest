from django.urls import path, include
from rest_framework import routers

from .views import HeroViewSet

router = routers.SimpleRouter()
router.register(r'heros', HeroViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
