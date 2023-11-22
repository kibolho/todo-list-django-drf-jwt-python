from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, ChangePasswordView, ProfileView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('me', ProfileView.as_view(), name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('change-password', ChangePasswordView.as_view(), name='password'),
    path('token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]