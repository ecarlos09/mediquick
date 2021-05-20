
from django.db import models

#get stored user model
from django.contrib.auth import get_user_model
User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    # define amount of messages to load 
    #load most recent 30 messages
    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]



# # # from django.contrib.auth.models import AbstractBaseUser

# from users.models import CustomUser
# from django.db.models import (Model, TextField, DateTimeField, ForeignKey, CASCADE)
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer

# class Room(models.Model):
#     room = models.CharField(max_length=100)
#     users = models.IntegerField(default=0)
 
#     def __str__(self):
#         return self.rname



# class MessageModel(Model):

#     user = ForeignKey(CustomUser, on_delete=CASCADE, verbose_name='user',
#                       related_name='from_user', db_index=True)
#     recipient = ForeignKey(CustomUser, on_delete=CASCADE, verbose_name='recipient',
#                            related_name='to_user', db_index=True)
#     timestamp = DateTimeField('timestamp', auto_now_add=True, editable=False,
#                               db_index=True)
#     body = TextField('body')

#     def __str__(self):
#         return str(self.id)

#     # def characters(self):
#     #     """
#     #     Toy function to count body characters.
#     #     :return: body's char number
#     #     """
#     #     return len(self.body)

#     def notify_ws_clients(self):
#         """
#         Inform client there is a new message.
#         """
#         notification = {
#             'type': 'recieve_group_message',
#             'message': '{}'.format(self.id)
#         }

#         channel_layer = get_channel_layer()
#         print("user.id {}".format(self.user.id))
#         print("user.id {}".format(self.recipient.id))

#         async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
#         async_to_sync(channel_layer.group_send)("{}".format(self.recipient.id), notification)

#     def save(self, *args, **kwargs):
#         """
#         Trims white spaces, saves the message and notifies the recipient via WS
#         if the message is new.
#         """
#         new = self.id
#         self.body = self.body.strip()  # Trimming whitespaces from the body
#         super(MessageModel, self).save(*args, **kwargs)
#         if new is None:
#             self.notify_ws_clients()

#     # Meta
#     class Meta:
#         app_label = 'chat'
#         verbose_name = 'message'
#         verbose_name_plural = 'messages'
#         ordering = ('-timestamp',)
