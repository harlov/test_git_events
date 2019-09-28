from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'authors', views.AuthorsViewSet)
router.register(r'repos', views.ReposViewSet)
router.register(r'events', views.EventsViewSet)
urlpatterns = router.urls
