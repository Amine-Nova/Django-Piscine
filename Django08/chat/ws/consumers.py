import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class chatConsumer (WebsocketConsumer):
    active_users = {}

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )
        if self.room_name not in self.active_users:
            self.active_users[self.room_name] = set()
        self.active_users[self.room_name].add(str(self.scope['user']))
        self.accept()
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type' : "connected_user",
                'user' : str(self.scope['user']),
                'active': list(self.active_users[self.room_name]),
            }
        )

    def disconnect(self, code):
        self.active_users[self.room_name].discard(str(self.scope['user']))
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                'type' : "disconnected_user",
                'user' : str(self.scope['user']),
                'active': list(self.active_users[self.room_name]),
            }
        )
    
    def receive(self, text_data = None, bytes_data = None):
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                "type" : "diff_message",
                'user' : str(self.scope['user']),
                "message" : text_data

            }
        )
    
    def diff_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type' : 'chat',
            'user' : event['user'],
            'message' : message
        }))

    def connected_user(self, event):
        self.send(text_data=json.dumps({
            'type' : 'connected',
            'user' : event['user'],
            'active' : event['active'],
        }))


    def disconnected_user(self, event):
        self.send(text_data=json.dumps({
            'type' : 'disconnected',
            'user' : event['user'],
            'active' : event['active'],
        }))