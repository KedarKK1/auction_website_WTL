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
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

# from django.contrib.auth.decorators import login_required

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
# TODO - here make sure to have a validation error incase the auction with that id does not exist
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    # queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        auction = AuctionModel.objects.get(id = self.kwargs.get('pk'))
        return QuestionModel.objects.filter(belongs_to_auction = auction)

    def perform_create(self, serializer):
        auction = AuctionModel.objects.get(pk=self.kwargs['pk'])
        serializer.save(question_owner=self.request.user,
                        belongs_to_auction=auction)


class QuestionRetrieveAPIView(generics.RetrieveAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer


class AnswerListAPIView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        # answer = AnswerModel.objects.get(belongs_to_question = self.kwargs.get('question_id') and id = self.kwargs.get('answer_id')) # ^ Note - here .get gives only one result, hence use filter
        answers = AnswerModel.objects.filter(belongs_to_question = self.kwargs.get('pk') )
        return answers
    
    def perform_create(self, serializer):
        # answer = AnswerModel.objects.get(pk = self.kwargs['pk'])
        # serializer.save(answer_owner = self.request.user, belongs_to_question = self.kwargs.get('pk'), belongs_to_auction = answer)
        question = QuestionModel.objects.get(id = self.kwargs.get('pk') ) 
        serializer.save(answer_owner = self.request.user, belongs_to_question = question )

class AnswerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionSerializer

# class BidListAPIView(generics.ListCreateAPIView):
#     queryset = BidModel.objects.all()
#     serializer_class = BidSerializer
#     permission_classes = [IsAuthenticated, ]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         self.perform_create(serializer)
#         bid_data = serializer.data
#         channel_layer = get_channel_layer()
#         async_to_sync(channel_layer.group_send)(
#             f"auction_{bid_data['belongs_to_auction']}",
#             {
#                 "type": "bid.message",
#                 "data": bid_data,
#             }
#         )
#         return Response(serializer.data, status = "201")

class BidAPIView(APIView):
    serializer_class = BidSerializer

    def post(self, request, auction_id):
        # auction = get_object_or_404(AuctionModel, id = auction_id)
        auction = AuctionModel.objects.get(id = auction_id)
        user = request.user
        if not user.is_authenticated:
            return Response({
                'detail': 'Authentication credentials were not provided.',
            },
            status = "401",
            )
        
        # Check bid price is at least 1rs higher than previous bid
        last_bid = BidModel.objects.filter(belongs_to_auction = auction_id).order_by('-bid_time').first()
        if(last_bid):
            if(int(request.data['curr_price']) <= int(last_bid.curr_price)):
                return Response({'detail': 'Bid price must be at least higher than current highest bid.'}, status = "400")
            
        # Check bid time is within 90 seconds from previous bid
        if(last_bid):
            if((timezone.now() - last_bid.bid_time) > timedelta(seconds = 90)):
                return Response({'detail': 'Bid time must be within 90 seconds from previous bid.'}, status = "400",)
            
        # Create new bid
        if not last_bid:
            if(int(request.data['curr_price']) <= int(auction.base_price)):
                return Response({'detail': 'Bid price must be at least higher than current highest bid.'}, status = "400")
        else:
            bid = BidModel.objects.create(
                belongs_to_auction = auction,
                curr_price = request.data['curr_price'],
                curr_bidder = user
            )

        # Update auction's current price
        # auction.curr_price = bid.curr_price
        # auction.save()

        # Send new bid data to WebSocket clients
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "auction_%d" % auction.id,
            {
                "type": "new_bid",
                "bid_id": bid.id,
                "curr_price": str(bid.curr_price),
                "curr_bidder": bid.curr_bidder.username
            },
        )

        return Response({'detail': 'Bid created successfully.'}, status = "201")
    
    def get(self, request, auction_id):
        # auction = get_object_or_404(AuctionModel, id = auction.id)
        auction = AuctionModel.objects.filter(id = auction_id)
        last_bid = BidModel.objects.filter(belongs_to_auction = auction_id).order_by('-bid_time').first()
        if(last_bid):
            data = {
                'curr_price': last_bid.curr_price,
                'curr_bidder': last_bid.curr_bidder.username,
            }
            return Response(data, 
                            status = "200"  
                            )
        else:
            return Response(
                {'detail': 'No bids have been made for this auction yet.'},
                status = "200",
            )
        
class AuctionAPIView(APIView):
    def get(self, request):
        auctions = AuctionModel.objects.all()
        data = []
        for auction in auctions:
            last_bid = BidModel.objects.filter(belongs_to_auction = auction.id).order_by('-bid_time').first()
            if(last_bid):
                curr_price = last_bid.curr_price
                curr_bidder = last_bid.curr_bidder.username
            else:
                curr_price = auction.base_price
                curr_bidder = "No bids yet"
            
            auction_data = {
                'id': auction.id,
                'name': auction.name,
                'auction_date': auction.auction_date,
                'base_price': auction.base_price,
                'curr_price': curr_price,
                'curr_bidder': curr_bidder
            }
            data.append(auction_data)
        return Response(data, status = "200")





