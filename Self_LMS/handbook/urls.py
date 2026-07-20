from django.contrib import admin
from django.urls import path
from . import views as views
urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.home, name = "home"),

    path('base', views.base, name = 'base'),

    path('courses', views.courses, name='courses'),

    path('courses/<slug:course_slug>/', views.course_detail, name='course_detail'),

    path('c1', views.c1, name = 'c1'),

    path('c2', views.c2, name = 'c2'),

    path('c3', views.c3, name = 'c3'),

    path('c4', views.c4, name = 'c4'),

    path('c5', views.c5, name = 'c5'),

    path('c6', views.c6, name = 'c6'),

    


]