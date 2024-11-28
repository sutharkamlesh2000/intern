"""
URL configuration for my_project project.

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
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.index,name="index")
    path('',views.StudentList.as_view(),name="student_list"),
    path('create/student/',views.StudentCreate.as_view(),name="student_create"),
    path('get/stundet/details',views.StudentDetails.as_view(),name="get_studnet_details"),
    path('delete/student/',views.DeleteStudent.as_view(),name="delete_student"),
    path('update/student/',views.UpdateStudent.as_view(),name="update_student"),
]
