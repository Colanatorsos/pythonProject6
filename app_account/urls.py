from django.urls import path
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()


app_name = "clients"
urlpatterns = [

    path("list/user/", UserListView.as_view(), name="list_user"),
    path("update/user/<int:pk>/", UserUpdateView.as_view(), name="update_user"),
    path("delete/user/<int:pk>/", UserDeleteView.as_view(), name="delete_user"),
    
    path("register/user/", RegisterUserView.as_view(), name="register_user"),
    path("login/user/", LoginUserView.as_view(), name="login_usser"),
    path(
        "confirm-email/<str:token>/", ConfirmEmailView.as_view(), name="confirm_email"
    ),
    path(
        "reset-password/user/",
        RequestPasswordResetView.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password-confirm/user/<str:uidb64>/<str:token>/",
        ResetPasswordConfirmView.as_view(),
        name="reset-password-confirm",
    ),
] + router.urls
