from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'project', ProjectViewSet, basename="project")
router.register(r'technology', TechnologyViewSet, basename="technology")
router.register(r'about', AboutViewSet, basename='about')
router.register(r'contact', ContactViewSets, basename="contact")
router.register(r'learning', LearningViewSets, basename="learning")

urlpatterns = router.urls
