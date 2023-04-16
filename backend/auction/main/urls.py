# from main.views import AuctionViewset, QuestionViewset, QuestionListCreateAPIView, QuestionRetrieveAPIView
from main.views import AuctionViewset, QuestionListCreateAPIView, QuestionRetrieveAPIView
from rest_framework import routers
from django.urls import path, include
from .views import *
from . import views

router = routers.DefaultRouter()  # DefaultRouter is similar to router SimpleRouter(), but have additionally includes a default API root view, that returns a response containing hyperlinks to all the list views

# router.register('description', DescriptionViewset, basename='description-url')

# below working
router.register('auction', AuctionViewset, basename='auction-url')
# my_model_viewset = QuestionViewset.as_view({'get': 'list', 'post': 'create', 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
# my_model_viewset = QuestionViewset.as_view({'post': 'create', 'get': 'retrieve'}) # Used for Mixins like ListCreateMixins, etc

urlpatterns = [
    path('', include(router.urls)),
    path('fav', views.favourite_add, name="edit_fav"),
    # path('<int:pk>/question/', my_model_viewset, name='question-url'),
    path('auctions/<int:pk>/questions/', QuestionListCreateAPIView.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionRetrieveAPIView.as_view(), name='question-retrieve'),
    path('answers/<int:pk>', AnswerListAPIView.as_view(), name='answer-list-create'),
    path('answer/<int:pk>', AnswerRetrieveAPIView.as_view(), name='answer-retrieve'),
]

# this also working

# urlpatterns = [
#     # path("<int:owner_id>/", AuctionViewset.as_view(), name="register"),
#     path("", AuctionViewset.as_view(), name="auctionurl"),
#     # path("stats", GetStatsAPI.as_view(), name="dashboard_stats"),
# ]
