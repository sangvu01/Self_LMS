from django.urls import path
from . import views

urlpatterns = [
    path('preview/', views.quiz_preview, name='quiz_preview'),
    path('preview/result/', views.quiz_preview_result, name='quiz_preview_result'),
    path('<int:question_id>/', views.quiz_view, name='quiz_view'),
    path('<int:question_id>/submit/', views.submit_answer, name='submit_answer'),
path(
    'preview/submit/',
    views.quiz_preview_submit,
    name='quiz_preview_submit',
),
]