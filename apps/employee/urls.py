from apps.employee.views import EmployeeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', EmployeeView, basename='user')
urlpatterns = router.urls