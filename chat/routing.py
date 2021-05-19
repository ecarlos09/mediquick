# from . import consumers

# from django.conf.urls import url

# websocket_urlpatterns = [
#     url(r'^ws$', consumers.ChatConsumer),
# ]



from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/available-doctors/$', consumers.LobbyConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]