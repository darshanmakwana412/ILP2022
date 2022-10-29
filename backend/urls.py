from django.contrib import admin
from django.urls import path
from . import views
from backend.views import PhonathonViewSet

urlpatterns = [
    path('', views.home,),
    # path('login', views.login1, name='login1'),
    # path('register', views.register, name='register'),
    # path('projects/', views.projects, name='projects'),
    # path('projects/update', views.update, name='update'),
    path('csv_profile', views.csv_profile, name='csv_profile'),
    path('csv_projects', views.csv_projects, name='csv_projects'),
    path('phonathon', views.Phonathon_save, name='phonathon'),
    # path('', views.down,),

]
