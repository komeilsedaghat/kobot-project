from django.urls import path
from .views import RegisterUserView,LogoutView,ProfileView,BlockUserView,PassResetView,PassResetDoneView,PassResetConfirm,PassResetComplete,ReportUserView

app_name = 'account'

urlpatterns = [
    path('register/',RegisterUserView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),


    path('reset_password/',PassResetView.as_view(),name='password-reset'),
    path('reset_password/done/',PassResetDoneView.as_view(),name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/',PassResetConfirm.as_view(),name='password_reset_confirm'),
    path('reset_password/complete/',PassResetComplete.as_view(),name='password_reset_complete'),


    path('profile/<str:username>/',ProfileView.as_view(),name='profile'),
    path('block/<str:username>/',BlockUserView.as_view(),name = 'block-user' ),
    path('report/<str:username>/<str:text>/',ReportUserView.as_view(),name='report'),



]