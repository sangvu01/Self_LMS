from django.contrib import admin
from django.urls import path
from . import views as views
from .views import CourseListAPIView, CourseDetailAPIView, ChapterAPIView
urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.home, name = "home"),

    path('base', views.base, name = 'base'),

    path('courses/', views.courses, name='courses'),

    path('courses/<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('courses/<slug:course_slug>/<slug:chapter_slug>/', views.chapter_detail, name='chapter_detail'),
    path("api/courses/", CourseListAPIView.as_view(), name="api-courses"),
    path("api/courses/<slug:course_slug>/", CourseDetailAPIView.as_view(), name="api-courses-id"),
    path("api/courses/<slug:course_slug>/<slug:chapter_slug>/", ChapterAPIView.as_view(), name = "api-chapter-detail")
]