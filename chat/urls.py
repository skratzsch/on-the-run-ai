from rest_framework import routers
from .views import ChatViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls