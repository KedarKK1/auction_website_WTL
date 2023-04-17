import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auction.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        # Just HTTP for now. (We can add other protocols later.)
    }
)


# """
# ASGI config for auction project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
# """

# import os

# # from channels.routing import ProtocolTypeRouter
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# # from channels.auth import AuthMiddlewareStack
# # from channels.security.websocket import AllowedHostsOriginValidator
# # from myapp.routing import websocket_urlpatterns
# # from django.urls import re_path

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auction.settings')

# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

# # application = ProtocolTypeRouter({
# #     # "http": django_asgi_app, # Empty for now (http->django views is added by default)
# #     # Just HTTP for now. (We can add other protocols later.)
# #     "websocket": AuthMiddlewareStack(  # adding these for websockets
# #         URLRouter(
# #             auction.routing.websocket_urlpatterns
# #             # websocket_urlpatterns
# #         )
# #     ),
# # })

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         # Just HTTP for now. (We can add other protocols later.)
#         # "websocket": AllowedHostsOriginValidator(
#         #     AuthMiddlewareStack(
#         #         URLRouter([
#         #             re_path(r"^front(end)/$", consumers.AsyncChatConsumer.as_asgi()),
#         #         ])
#         #     )
#         # ),
#     }
# )


# # application = get_asgi_application() # original content
