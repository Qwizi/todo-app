from rest_framework import routers

from users.views import UserViewSet
from todos.views import TodoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet, base_name='todos')

urlpatterns = router.urls
