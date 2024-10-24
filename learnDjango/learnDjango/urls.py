"""
URL configuration for learnDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-page/',views.about),
    path('',views.home,name='home'),
    path('index-page/',views.index,name='index'),
    path('main-page/',views.main),
    path('courses/',views.courses),
    path('student/',views.student),
    path('index/',views.index),
    path('students/',views.students,name='student'),
    path('teacher/',views.teacher),
    path('book/',views.book),
    path('product/',views.product),
    path('employee/',views.employee),
    path('class-based-view/',views.MyView.as_view(),name="class-based-view"),
   
]
