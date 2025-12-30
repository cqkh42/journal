# auth_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class CloudflareAccessBackend(BaseBackend):
    def authenticate(self, request):
        if not request:
            return None

        email = request.META.get(
            "HTTP_CF_ACCESS_AUTHENTICATED_USER_EMAIL"
        )
        if not email:
            return None

        user, _ = User.objects.get_or_create(
            email=email,
            defaults={"username": email},
        )
        return user

    def get_user(self, user_id):
        return User.objects.filter(pk=user_id).first()