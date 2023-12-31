from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from django.contrib.auth import login, authenticate

from .models import User
from .serializers import (
    UserSerializer,
    LoginUserSerializer,
    ResetPasswordConfirmSerializer,
)

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


class RequestPasswordResetView(APIView):
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "Пользователь с таким email не найден"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        uid = urlsafe_base64_encode(force_str(user.pk).encode())
        token = default_token_generator.make_token(user)

        reset_url = reverse(
            "clients:reset-password-confirm", kwargs={"uidb64": uid, "token": token}
        )
        reset_url = request.build_absolute_uri(reset_url)

        subject = "Восстановление пароля"
        message = f"Для восстановления пароля перейдите по ссылке: {reset_url}"

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

        return Response(
            {"success": "Ссылка для восстановления пароля отправлена на ваш email"}
        )


class ResetPasswordConfirmView(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={"uidb64": kwargs["uidb64"], "token": kwargs["token"]},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        try:
            serializer.save()
            return Response({"success": "Пароль успешно изменен"})
        except:
            return Response(
                {"error": "Недействительная ссылка для сброса пароля"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()

        return Response(
            {
                "detail": "Registration successful",
                "user_id": client.id,
                "email": client.email,
                "username": client.username,
            },
            status=status.HTTP_201_CREATED,
        )

class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        if email and password:
            client = authenticate(email=email, password=password)

            if client:
                login(request, client)
                refresh = RefreshToken.for_user(client)
                return Response(
                    {
                        "user_id": client.id,
                        "email": client.email,
                        "username": client.username,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "detail": "Authentication failed. User not found or credentials are incorrect."
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Invalid input. Both email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, token):
        try:
            user = User.objects.get(activation_token=token)
            user.is_active = True
            user.save()
        except User.DoesNotExist:
            raise ({"error": "invalid-token"})


class ConfirmEmailView(generics.GenericAPIView):
    @staticmethod
    def get(request, token):
        try:
            user = User.objects.get(token_auth=token)
            if user.is_active:
                return Response(
                    {"detail": "User is already activated"}, status=status.HTTP_200_OK
                )

            user.is_active = True
            user.save()

            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "detail": "Email confirmation successful",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        except User.DoesNotExist:
            return Response(
                {"detail": "Invalid token"}, status=status.HTTP_404_NOT_FOUND
            )



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =  [permissions.IsAdminUser]


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =  [permissions.IsAdminUser]

    
