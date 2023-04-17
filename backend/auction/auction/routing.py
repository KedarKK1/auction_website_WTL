# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/auction/(?P<auction_id>\d+)/$', consumers.BidConsumer.as_asgi()),
# ]

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('chatroompage', consumers.ChatConsumer),
]