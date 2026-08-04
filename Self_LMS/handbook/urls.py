from django.contrib import admin
from django.urls import path
from . import views as views
from .views import CourseListAPIView, CourseDetailAPIView
urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.home, name = "home"),

    path('base', views.base, name = 'base'),

    path('courses/', views.courses, name='courses'),

    path('courses/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('courses/<slug:course_slug>/<slug:chapter_slug>/', views.chapter_detail, name='chapter_detail'),
    
    path('course/<slug:course_slug>/result/', views.quiz_result, name='quiz_result'),
    path('course/<slug:course_slug>/quiz/<int:quiz_id>/', views.quiz_id, name='quiz_detail'),
    path('course/<slug:course_slug>/retake/', views.retake_quiz, name='retake_quiz'),
    path('course/<slug:course_slug>/start/', views.start_quiz, name='start_quiz'),


    path("api/courses/", CourseListAPIView.as_view(), name="api-courses"),
    path("api/courses/<slug:course_slug>/", CourseDetailAPIView.as_view(), name="api-courses-id"),
]