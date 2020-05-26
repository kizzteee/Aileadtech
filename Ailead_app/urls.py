from django.urls import path
from Ailead_app import views
from django.contrib.auth import views as auth_views

app_name = 'Ailead_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('whatsnew/', views.whatsnew, name='whatsnew'),
    path('logout/', views.user_logout, name='logout'),
    path('ecommerce/', views.ecommerce, name='ecommerce'),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="Ailead_app/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="Ailead_app/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="Ailead_app/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="Ailead_app/password_reset_done.html"),
        name="password_reset_complete"),

    path('success/', views.success, name='success'),

]
