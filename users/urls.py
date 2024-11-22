from rest_framework.routers import DefaultRouter


from . import views

router = DefaultRouter()

router.register('user', views.UserViewSet, basename='user')
router.register('auth', views.AutehnticateViewSet, basename='auth')


urlpatterns = router.urls