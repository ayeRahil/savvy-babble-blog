from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit_account/', views.UserEditView.as_view(), name='edit-account'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password-change'),
    path('password/', views.PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='password-change'),
    path('<int:pk>/edit_profile', views.EditProfileView.as_view(), name='edit-profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create-profile'),

]