import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
#get stored user model
from django.contrib.auth import get_user_model
User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self,data):
        messages = Message.last_10_messages()
        content = {
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author = data['from'] #logged in user username
        author_user = User.objects.filter(username=author)[0]
        message = Message.objects.create(
            author=author_user,
            content=data['message'])
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    # create json data array
    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    #serialize
    def message_to_json(self, message):
        return {
            'author': message.author.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive historic messages
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        #message = data['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # send historic messages
    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # handle the message: send
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))



# class LobbyConsumer(AsyncWebsocketConsumer):
#     @database_sync_to_async
#     def available_roooms(self):
#         serialized_data = serializers.serialize("json", Room.objects.filter(users=1))
#         return serialized_data
        

#     async def connect(self):
#         await self.accept()
        
#         while True:
#             l = await self.available_roooms()
#             await self.send(text_data = l)