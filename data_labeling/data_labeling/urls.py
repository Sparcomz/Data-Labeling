"""
URL configuration for data_labeling project.

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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
    path('uploader/', views.home_view, name='uploader_home'),  # Reuse home_view for uploader
    path('upload/', views.upload_data_view, name='upload_data'),
    path('annotator/', views.home_view, name='annotator_home'),  # Reuse home_view for annotator
    path('annotate/<int:task_id>/', views.annotate_task_view, name='annotate_task'),
]
