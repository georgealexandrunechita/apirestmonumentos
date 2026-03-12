from django.db.models.functions import Lower

from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Monument
from .serializers import MonumentSerializer, RegisterSerializer


class MonumentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50


class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class MonumentViewSet(ModelViewSet):
    queryset = Monument.objects.all()
    serializer_class = MonumentSerializer
    pagination_class = MonumentPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(name__icontains=query)

        sort = self.request.GET.get("sort", "name")
        allowed_fields = ["name", "location", "year", "id"]
        if sort.lstrip("-") in allowed_fields:
            if sort.lstrip("-") == "name":
                direction = "-" if sort.startswith("-") else ""
                queryset = queryset.order_by(direction + "name")
            else:
                queryset = queryset.order_by(sort)

        return queryset
