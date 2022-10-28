from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from mentors.users.api.views import UserViewSet, LoadUserView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
urlpatterns += [
    path("users/me/", LoadUserView.as_view()),
]
