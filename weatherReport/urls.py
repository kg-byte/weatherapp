from django.urls import path
from . import views

urlpatterns = [
				path('users/new', views.new_user, name='userinfo'),
				path('dashboard/<int:user_id>', views.dashboard, name='dashboard'),
				]

