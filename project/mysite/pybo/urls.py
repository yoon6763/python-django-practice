from . import views
from django.urls import path

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.details, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name="answer_create"),
    path('question/create/', views.question_create, name="question_create")
]
