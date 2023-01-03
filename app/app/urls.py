from django.urls import path, include
from . import views 

urlpatterns = [
    path('index', views.index, name='index'),
    path('search_results', views.search_results, name="search_results"),
    path('create_question', views.create_question, name="create_question"),
    path('read_question/<int:id>', views.read_question, name='read_question'),
    path('open_create_question_form', views.open_create_question_form, name="open_create_question_form"),
    path('submit_answer', views.submit_answer, name="submit_answer")
]
