
from channels.staticfiles import StaticFilesConsumer
from chat import consumers

channel_routing = {
    # This makes Django serve static files from settings.STATIC_URL, similar
    # to django.views.static.serve. This isn't ideal (not exactly production
    # quality) but it works for a minimal example.
    'http.request': StaticFilesConsumer(),

    # Wire up websocket channels to our consumers:
    'websocket.connect': consumers.connect,
    'websocket.receive': consumers.chat_message,
    'websocket.disconnect': consumers.disconnect,
}
