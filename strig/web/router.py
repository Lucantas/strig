from rest_framework.routers import DefaultRouter

from strig.web import views

router = DefaultRouter()

router.register(r"users", views.UserViewSet, basename="user")