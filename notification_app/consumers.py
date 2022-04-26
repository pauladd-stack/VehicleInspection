# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer

from django.contrib.auth import get_user_model

User = get_user_model()

class NotifConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #self.room_group_name = 'notification_%s' % self.room_name
        self.room_group_name = self.room_name
        print(self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        

    ''' await self.send(json.dumps({
            "type":"websocket.send",
            "text":self.room_name
        })) '''

    async def disconnect(self, close_code):
        # Leave room group
        await self.close(close_code)
        '''await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )'''


    # Receive message from room group
    async def send_notification(self, event):
        await self.send(event.get('value'))


'''
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        '''