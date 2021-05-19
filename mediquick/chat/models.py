# from django.db import models
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