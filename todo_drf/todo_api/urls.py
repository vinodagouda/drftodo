from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.authtoken import views as views2 # Django Default Authentication

from todo_api import views

router = routers.DefaultRouter()
router.register(r'todo', views.ToDoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # JWT Authentication
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # JWT refresh Authentication
    path('token_generate/', views2.obtain_auth_token), # Django default Authentication
]