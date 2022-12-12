from apps.task.views import TaskView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TaskView, basename='user')
urlpatterns = router.urls