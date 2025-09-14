from django.urls import path

from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('addvideo/',create_post,name='create-post'),
    path('user/<int:id>/', user_get_by_id, name='user_by_id'),
]
