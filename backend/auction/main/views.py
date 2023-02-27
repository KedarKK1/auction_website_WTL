from django.shortcuts import render
from .models import *
from authapp.models import *
from .serializers import *
# from rest_framework.views import APIView, Response
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated

# Class-based views — Inherits the APIView class
# Function-based views — Uses the @api_view decorator

# Django’s generic views - use classes & mixins to quickly write common views of data without having to repeat yourself.
# certain class attributes — queryset, serializer_class - to define which resource you want

# ViewSets - combination with Router to set of consistent URL configurations and to ensure DRY
# gives you a set of actions e.g. list, update to work with instead of handlers e.g. get, post and the Router automatically creates urls for all actions

# define these actions yourself (GenericViewSet)
# use something that implements common read & write actions out-of-the-box (ModelViewSet)

# list (GET), create(POST), retrieve (GET), update (PUT), partial_update(PATCH), destroy (DELETE)
# all Generic Views inherit from GenericAPIView .
# Generic Views - 1. ListCreateAPIView(ListCreateAPIView combines the two functionalities list & create inheriting from ListModelMixin & CreateModelMixin)
# ViewSets - ModelViewSet creates all 6 common read-write operations mentioned above

# ViewSets as it provides a lot of functionality out of the box with very little code involved and start overwriting methods to allow more specialized functionality. When your needs expand, start overwriting the standard ViewSet functions to gradually fit your needs.
# Use Views for very specific use cases or building some quick endpoints if necessary.
# Use Generic views & Mixins when you need some features out-of-the-box but don’t want to implement all actions provided by ViewSets


# class DescriptionViewset(ListModelMixin, CreateModelMixin, RetrieveModelMixin, GenericViewSet):
#     queryset = Description.objects.all()
#     serializer_class = DescriptionSerializer

class AuctionViewset(ListModelMixin, CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = AuctionModel.objects.all()
    serializer_class = AuctionCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
