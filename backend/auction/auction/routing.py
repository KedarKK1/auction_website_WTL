# from django.urls import re_path
# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/auction/(?P<auction_id>\d+)/$', consumers.BidConsumer.as_asgi()),
# ]

from django.urls import path, re_path
from . import consumers

# websocket_urlpatterns = [
#     path('chatroompage', consumers.ChatConsumer),
# ]

websocket_urlpatterns = [
    # re_path(r'ws/bidauction/(?P<auction_id>\d+)/$',
    # re_path(r'chatroompage',
    re_path(r'ws/auctions/(?P<auction_id>\d+)/bids/$', 
    consumers.BidConsumer.as_asgi()),
]
