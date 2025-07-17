from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ModuleViewSet, LessonViewSet

router = DefaultRouter()
router.register('', CourseViewSet)
router.register('modules', ModuleViewSet)
router.register('lessons', LessonViewSet)

urlpatterns = router.urls
