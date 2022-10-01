from django.urls import path, include
from .views import RegisterView, UserDetailView

urlpatterns = [
    path("", include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view(), name="register"),
    path('userdetail/<int:pk>/', UserDetailView.as_view()),
]
