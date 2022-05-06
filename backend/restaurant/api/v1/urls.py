from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HotButtonViewSet, RestaurantViewSet

router = DefaultRouter()
router.register("restaurant", RestaurantViewSet)
router.register("hotbutton", HotButtonViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
