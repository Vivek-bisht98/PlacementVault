from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_page),

    path('login/', views.login_page),

    path('register/', views.register_page),

    path('dashboard/', views.dashboard),

    path('logout/', views.logout_page),

    path('add-schedule/', views.add_schedule),

    path('publish-experience/', views.publish_experience),

    path('search/', views.search_company),

    path(
    'role/<str:role>/',
    views.role_page
),
    path(
    'round/<str:role>/<str:round_type>/',
    views.round_page
),
    path(
    'experience/<str:role>/<str:round_type>/<str:focus_subject>/',
    views.experience_page
),
    path(
    'edit-experience/<int:id>/',
    views.edit_experience
),

path(
    'delete-experience/<int:id>/',
    views.delete_experience
),
]