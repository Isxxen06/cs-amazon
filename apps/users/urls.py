from django.urls import path
from .views import UserRegisterAPIView, UserDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name="user-register"),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
