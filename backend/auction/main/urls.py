from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter() # DefaultRouter is similar to router SimpleRouter(), but have additionally includes a default API root view, that returns a response containing hyperlinks to all the list views

# router.register('description', DescriptionViewset, basename='description-url')
router.register('auction', AuctionViewset, basename='auction-url')

urlpatterns = [
    path('', include(router.urls))
]