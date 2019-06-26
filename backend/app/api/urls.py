from rest_framework import routers

from .views import TodoViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
