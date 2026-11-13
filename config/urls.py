from django.urls import path, include
from rest_framework.routers import DefaultRouter
from animales.views import AnimalViewSet
router = DefaultRouter()
router.register("animales", AnimalViewSet, basename="animal")
urlpatterns = [path("api/", include(router.urls))]
