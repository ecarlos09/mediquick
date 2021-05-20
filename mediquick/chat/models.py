# from django.db import models

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
# from django.conf import settings 

# class PrivateChatRoom(models.Model):
#     title = models.CharField(max_length=255, unique=True, blank=False)
#     users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text="users who are connected to chat")

#     def __str__(self):
#         return self.title
    
#     def connect_user(self, user):
#         is_user_added = False
#         if not user in self.users.all():
#             self.users.add(user)
#             self.save()
#             is_user_added = True
#         elif user in self.users.all():
#             is_user_added = True
#         return is_user_added 

#     def disconnect_user(self, user):
#         """
#         return true if user is removed from the users list
#         """
#         is_user_removed = False
#         if user in self.users.all():
#             self.users.remove(user)
#             self.save()
#             is_user_removed = True
#         return is_user_removed

#     @property
#     def group_name(self):
#         """
#         returns channels group name that sockets should subscribe to as messages generated
#         """
#         return f"PrivateChatRoom-{self.id}"

# class PrivateRoomChatMessageManager(models.Manager):
#     def by_room(self, room):
#         qs = PrivateRoomChatMessage.objects.filter(room=room).order_by("timestamp")
#         return qs


# class PrivateRoomChatMessage(models.Model):
#     """
#     chat message created by a user
#     """
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     room = models.ForeignKey(PrivateChatRoom, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     content = models.TextField(unique=False, blank=False)

#     objects = PrivateRoomChatMessageManager()

#     def __str__(self):
#         return self.content
