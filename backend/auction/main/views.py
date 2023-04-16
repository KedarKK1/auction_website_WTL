from django.shortcuts import render
from .models import *
from authapp.models import *
from .serializers import *
# from rest_framework.views import APIView, Response
from rest_framework import mixins, viewsets, generics
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response


# CreateModelMixin: Provides a create method for creating a new object instance.

# ListModelMixin: Provides a list method for retrieving a list of object instances.

# RetrieveModelMixin: Provides a retrieve method for retrieving a single object instance.

# UpdateModelMixin: Provides update and partial_update methods for updating an existing object instance.

# DestroyModelMixin: Provides a destroy method for deleting an object instance.

# ReadOnlyModelViewSet: A viewset that combines the ListModelMixin and RetrieveModelMixin to provide read-only views.

# ModelViewSet: A viewset that includes all of the CRUD operations (list, create, retrieve, update, partial_update, and destroy) using the appropriate mixins.

# GenericViewSet: A viewset that does not include any default actions or methods. You can mix in any combination of mixins to create a custom viewset.

# GenericAPIView: A base class for views that provides some common functionality, such as pagination, filtering, and serializer validation.

# ViewSetMixin: A mixin that provides some common functionality, such as setting the queryset and serializer class, for use in custom viewsets.

# These mixins can be used in combination to create custom views and viewsets that provide the necessary functionality for your API.


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

# class AuctionViewset(ListModelMixin, CreateModelMixin, RetrieveModelMixin, GenericViewSet): # For CRU operations only
# for CRUD operations # here for PUT operation, we get prefilled forms
class AuctionViewset(ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    # class AuctionViewset(generics.RetrieveUpdateDestroyAPIView, generics.ListCreateAPIView): # also worked, this have CRUD Functionality, but gives me error at the time of getting multiple objects
    queryset = AuctionModel.objects.all()
    serializer_class = AuctionCreateSerializer
    permission_classes = [IsAuthenticated]
    # lookup_field = 'owner_id' # update the lookup field name

    # filtering
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'description_location']
    filterset_fields = ['base_price', 'auction_date']

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


def favourite_add(self, arg, args):
    return ({ans: "HI"})


# class QuestionViewset(ListModelMixin, CreateModelMixin, GenericViewSet):
class QuestionListCreateAPIView(generics.ListCreateAPIView): # TODO - here make sure to have a validation error incase the auction with that id does not exist
    # queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        auction = AuctionModel.objects.get(id = self.kwargs.get('pk'))
        return QuestionModel.objects.filter(belongs_to_auction = auction)
    
    def perform_create(self, serializer):
        auction = AuctionModel.objects.get(pk = self.kwargs['pk'])
        serializer.save(question_owner = self.request.user, belongs_to_auction = auction)

class QuestionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

