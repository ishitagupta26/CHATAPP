from django.urls import path
from .views import RegisterView,LoginView
from users import views
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),


]