from django.urls import path

from users.views import RegisterView, LoginView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('<int:pk>/', UserView.as_view()),
]
