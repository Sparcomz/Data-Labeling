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
    path('uploader/', views.home_view, name='uploader_home'),
    path('upload/', views.upload_data_view, name='upload_data'),
    path('annotator/', views.home_view, name='annotator_home'),
    path('annotate/<int:task_id>/', views.annotate_task_view, name='annotate_task'),
    path('reviewer/', views.home_view, name='reviewer_home'),
    path('review/<int:task_id>/', views.review_task_view, name='review_task'),
    path('admin_home/', views.home_view, name='admin_home'),
    path('view_data/', views.view_data_list, name='view_data_list'),
    path('view_data/<int:data_id>/', views.view_data_detail, name='view_data_detail'),
    path('view_reviews/', views.view_review_list, name='view_review_list'),
    path('view_review/<int:review_id>/', views.view_review_detail, name='view_review_detail'),
    path('manage_user/', views.manage_user_view, name='manage_user'),
    path('view_feedback/<int:annotation_id>/', views.view_feedback_detail, name='view_feedback_detail'),
]
