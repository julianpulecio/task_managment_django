from rest_framework.routers import DefaultRouter

from apps.project.views import ProjectView

router = DefaultRouter()
router.register('', ProjectView, basename='project')
urlpatterns = router.urls