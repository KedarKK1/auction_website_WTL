from django.generic.websocket import AsyncWebsocketConsumer
import json
from .models import BidModel

class BidConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.auction_id = self.scope['url_route']['kwargs']['auction_id']
        self.bid_group_name = 'auction_%s_bid_updates' % self.auction_id

        # Join bid group
        await self.channel_layer.group_add(
            self.bid_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # leave bid group
        await self.channel_layer.group_discard(
            self.bid_group_name,
            self.channel_name,
        )

    # Receive bid update from webSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        bid_price = text_data_json['bid_price']

        # Update bid model
        auctionBelongsTo = BidModel.objects.get(id = self.auction_id)
        bid = BidModel.objects.create(
            belongs_to_auction = auctionBelongsTo,
            curr_price = bid_price, 
            curr_bidder = self.scope['user'].username
        )

        # Send bid update to bid group
        await self.channel_layer.group_send(
            self.bid_group_name,
            {
                'type': 'bid_update',
                'bid_id': bid.id,
                'bid_price': str(bid.curr_price),
                'curr_bidder': bid.curr_bidder,
                'bid_time': str(bid.bid_time)

            }
        )

        # Receive bid update from bid group
        async def bid_update(self, event):
            await self.send(text_data = json.dumps(event))